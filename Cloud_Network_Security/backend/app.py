from flask import Flask, request, render_template, redirect
import datetime, csv, os, pickle
import pandas as pd

app = Flask(__name__)

# ✅ Load ML model safely
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("✅ Model loaded successfully")
except Exception as e:
    print("❌ Model loading failed:", e)
    model = None

# ✅ Home route → Login page
@app.route('/')
def home():
    return render_template('login.html')

# ✅ Signup route with CSV logging
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        twofa = request.form.get('twofa', '')  # Optional
        signup_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print(f"🆕 New signup: {username}, {email}")

        # ✅ Save to CSV
        file_path = 'user_data.csv'
        file_exists = os.path.isfile(file_path)
        with open(file_path, 'a', newline='') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(['Username', 'Email', 'Password', '2FA Code', 'Signup Time'])
            writer.writerow([username, email, password, twofa, signup_time])

        return redirect('/dashboard')

    return render_template('signup.html')

# ✅ Login route
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == 'admin123':
        return redirect('/dashboard')
    else:
        return "Invalid login"

# ✅ Dashboard route
@app.route('/dashboard')
def dashboard():
    df = pd.read_csv('login_logs.csv')
    failed = df[df['failed_logins_24h'] > 0]
    hourly = failed['hour'].value_counts().sort_index()

    labels = [str(label) for label in hourly.index]
    values = [int(val) for val in hourly.values]

    return render_template('dashboard.html', labels=labels, values=values)

# ✅ Threats page
@app.route('/threat')
def threat():
    return render_template('threat.html')

# ✅ Firewall page
@app.route('/firewall')
def firewall():
    return render_template('firewall.html')

# ✅ Reports page
@app.route('/report')
def report():
    df = pd.read_csv('login_logs.csv')
    suspicious = df[df['failed_logins_24h'] > 5]
    summary = suspicious.groupby('ip_block')['failed_logins_24h'].sum().reset_index()
    summary.columns = ['ip', 'failed_attempts']
    summary = summary.sort_values(by='failed_attempts', ascending=False)
    ip_data = summary.to_dict(orient='records')
    return render_template('report.html', ip_data=ip_data)

# ✅ Logout route
@app.route('/logout')
def logout():
    return redirect('/')

# ✅ Helper: Log failed login attempts
def log_failed_attempt(ip, time):
    file_exists = os.path.isfile('login_logs.csv')
    with open('login_logs.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([
                'session_id', 'user_id', 'timestamp', 'country', 'device_type',
                'ip_block', 'failed_logins_24h', 'hour', 'country_changed',
                'is_new_ip', 'is_new_device', 'label_anomaly'
            ])
        writer.writerow([
            'session123', 'user01', time, 'IN', 'Mobile',
            ip, 1, datetime.datetime.now().hour, False,
            True, False, 1
        ])

# ✅ Helper: Count failed attempts for an IP
def get_failed_attempts(ip):
    count = 0
    if not os.path.isfile('login_logs.csv'):
        return count
    with open('login_logs.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['ip_block'] == ip and int(row['failed_logins_24h']) > 0:
                count += int(row['failed_logins_24h'])
    return count

# ✅ Helper: ML prediction for suspicious login
def is_suspicious(ip, time):
    if model is None:
        return False
    failed_attempts = get_failed_attempts(ip)
    prediction = model.predict([[failed_attempts, time]])
    return prediction[0] == 1

# ✅ Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5050)
