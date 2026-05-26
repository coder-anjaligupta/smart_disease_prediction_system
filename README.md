# 🩺 Smart Disease Prediction System

A simple and interactive health prediction web application built using **Python**, **Streamlit**, and **SQLite**.

This project helps users check possible health risks for:

- Diabetes
- Heart Disease
- Kidney Disease

The system includes:

✅ User Registration  
✅ Secure Login System  
✅ Password Recovery  
✅ Disease Prediction Dashboard  
✅ SQLite Database Integration  
✅ Interactive User Interface  

---

# 📌 Project Overview

The Smart Disease Prediction System is a healthcare web application that allows users to enter health details and get a prediction report.

The application calculates risk probability using custom prediction logic and displays the result in a clean and user-friendly dashboard.

This project is developed for academic learning and portfolio demonstration purposes.

---

# 🚀 Features

## 🔐 Authentication System
- New user registration
- Login system
- Password recovery using username and email
- Session management using Streamlit session state

## 🩺 Disease Prediction Modules

### 1. Diabetes Prediction
Checks risk using:
- Glucose Level
- Blood Pressure
- Age

### 2. Heart Disease Prediction
Checks risk using:
- Cholesterol Level
- Max Heart Rate
- ST Depression (Oldpeak)

### 3. Kidney Disease Prediction
Checks risk using:
- Blood Pressure
- Albumin Level
- Sugar Level

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Logic |
| Streamlit | Web Application Framework |
| SQLite3 | Database Management |
| NumPy | Numerical Operations |
| HTML/CSS | User Interface Design |

---

# 📂 Project Structure

```bash
Smart_Disease_Prediction_System/
│
├── app.py
├── auth.py
│
├── styles/
│   ├── login.css
│   ├── dashboard.css
│   └── logout.css
│
├── components/
│   └── header.html
│
└── users.db
````

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/coder-anjaligupta/Smart_Disease_Prediction_System.git
```

## 2️⃣ Open Project Folder

```bash
cd Smart_Disease_Prediction_System
```

## 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

## 4️⃣ Run Streamlit Application

```bash
streamlit run app.py
```

---

# ▶️ How the System Works

1. User creates a new account.
2. User logs into the portal.
3. User selects a disease type.
4. User enters health values.
5. System calculates risk probability.
6. Prediction result is displayed with progress bar and health report.

---

# 📊 Prediction Logic

The project currently uses a simple custom prediction formula:

```python
score = sum(values) / len(values)
risk_prob = min(max(score / 200, 0.1), 0.9)
```

This logic is used for educational and demonstration purposes only.

---

# 🎨 User Interface

The application includes:

* Modern dashboard design
* Responsive layout
* Interactive sliders
* Progress bars
* Sidebar navigation
* Custom CSS styling

---

# 🔒 Database Information

SQLite database is used for:

* Storing user accounts
* Login authentication
* Password recovery

Database Table:

```sql
userstable(username TEXT, email TEXT, password TEXT)
```

---

# 📸 Application Preview

## 🔐 Login & Registration Page

* User Registration
* Login Authentication
* Password Recovery

## 🩺 Dashboard

* Disease Selection
* Health Parameter Input
* Prediction Result
* Risk Analysis Report

---

# 📌 Future Improvements

* Add trained machine learning models
* Improve prediction accuracy
* Add downloadable health reports
* Add doctor recommendation feature
* Add cloud database support
* Improve security system

---

# ⚠️ Disclaimer

This project is developed for:

* Academic learning
* Practice purposes
* Portfolio demonstration

This system does NOT provide real medical advice.

Always consult a certified doctor for medical diagnosis.

---

# 👨‍💻 Author

Developed by: Anjali Gupta

---

# ⭐ GitHub Support

If you like this project:

⭐ Star the repository
🍴 Fork the project
📢 Share with others

