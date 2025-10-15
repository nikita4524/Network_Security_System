***Network Security System***

**1. Project Title**

Network Security System

**2. Description**

This project focuses on monitoring, analyzing, and securing network traffic using Flask and Python.
It helps identify suspicious activities, analyze network datasets, and provides an intuitive interface for users to visualize and manage network data.
The goal is to create an efficient system for threat detection, data protection, and secure network management.

**3. Features**

User authentication (Login/Signup)

 IP traffic monitoring

Dataset-based network traffic analysis

Suspicious connection detection

Interactive dashboard and visual reports

Responsive and user-friendly interface

**4. Tech Stack / Tools Used**

Backend: Python, Flask

Frontend: HTML, CSS, Bootstrap

Data Analysis: NumPy

Tools: Virtual Environment (venv), Command Line Interface

**5. Installation / Setup Instructions**

 Step 1: Go to the project folder
cd C:\Users\janhvi\Downloads\Cloud_Network_Security

 Step 2: Activate the virtual environment
venv\Scripts\activate

Step 3: Install required dependencies
pip install -r requirements.txt

Step 4: Run the Flask application
python app.py

Step 5: Open the application in your browser
http://127.0.0.1:5050/

**6. Usage**

Once the app is running:

Open your browser and go to http://127.0.0.1:5050/

Login or create a new account

Upload or analyze your network dataset

View real-time logs, suspicious IPs, and traffic patterns on the dashboard

**7. Screenshots**


**8. Project Structure**
Cloud_Network_Security/
│
├── app.py
├── clean_app.py
├── train_model.ipynb
│
├── templates/
│   ├── login.html
│   ├── Thread.html
│   ├── dashboard.html
│   └── Firewall.html
│
├── dataset/
│   ├── network_traffic.csv
│   ├── user_data.csv
│   └── login_logs.csv
│
├── requirements.txt
└── README.md

**9. Contributors / Team Members**
Name	Role
Janhvi Marathe	Backend Developer
Nikita Patil	Frontend & Documentation
Sejal Dorik	Data Analysis

**10. Dataset and Analysis**

The project uses a network traffic dataset to identify normal vs. suspicious activities within a network.
The dataset includes:

IP Addresses

Source & Destination Ports

Protocol Type

Label (Normal / Attack)


**11. Contact / Links**

GitHub Repository: https://github.com/nikita4524/Network_Security_System.git

