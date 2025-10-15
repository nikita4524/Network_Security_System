from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Flask is finally working!"

if __name__ == '__main__':
    app.run(debug=True, port=5050)
