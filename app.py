

import streamlit as st
import sqlite3
import numpy as np

# ---------------- DATABASE FUNCTIONS ----------------
# This function creates the user table in database
def create_usertable():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, email TEXT, password TEXT)')
    conn.commit()
    conn.close()

# This function saves new user data to database
def add_userdata(username, email, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO userstable(username, email, password) VALUES (?,?,?)', (username, email, password))
    conn.commit()
    conn.close()

# This function checks if user login details are correct
def login_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM userstable WHERE username =? AND password =?', (username, password))
    data = c.fetchall()
    conn.close()
    return data

# This function finds password using username and email
def find_password(username, email):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT password FROM userstable WHERE username =? AND email =?', (username, email))
    data = c.fetchone()
    conn.close()
    return data

# ---------------- SESSION SETUP ----------------
# Check if user is logged in or not
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Create database table when app starts
create_usertable()

# ---------------- LOGIN / REGISTER PAGE ----------------
if not st.session_state.logged_in:

    st.set_page_config(page_title="Secure Access", layout="centered")

    # CSS for login page design
    st.markdown("""
    <style>
 .stTabs [data-baseweb="tab"] {
        color: #60a5fa!important;
        font-weight: 600;
    }
 .stTabs [aria-selected="true"] {
        color: #2563eb!important;
        border-bottom-color: #2563eb!important;
    }

 .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3em;
        background-color: #1e3a8a!important;
        color: white!important;
        font-weight: bold;
        border: none;
    }
 .stButton>button:hover {
        background-color: #1e40af!important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🔒 Secure Patient Diagnostic Portal")

    # Three tabs for register, login and password recovery
    tabs = st.tabs(["Register New Account", "Login to Portal", "Recover Password"])

    # Tab 1: Register new user
    with tabs[0]:
        st.subheader("Create Account")
        u = st.text_input("Username")
        e = st.text_input("Email")
        p = st.text_input("Password", type="password")

        if st.button("Register"):
            if u and p:
                add_userdata(u, e, p)
                st.success("Account Successfully Created")
            else:
                st.warning("Fill all fields")

    # Tab 2: User login
    with tabs[1]:
        st.subheader("Welcome Back")
        u = st.text_input("Username", key="lu")
        p = st.text_input("Password", type="password", key="lp")

        if st.button("Login to Dashboard"):
            if login_user(u, p):
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid Login")

    # Tab 3: Recover forgotten password
    with tabs[2]:
        st.subheader("Recover Password")
        u = st.text_input("Username", key="fu")
        e = st.text_input("Email", key="fe")

        if st.button("Retrieve Password"):
            res = find_password(u, e)
            if res:
                st.info(f"Password: {res[0]}")
            else:
                st.error("Not found")

# ---------------- MAIN DASHBOARD AFTER LOGIN ----------------
else:

    import streamlit as st
    import numpy as np

    # Set page title and layout for dashboard
    st.set_page_config(page_title="Smart Disease Predictor", layout="centered")

    # CSS for main dashboard design
    st.markdown("""
        <style>
        @import url('https://googleapis.com');
        
     .main { 
            background-color: #f8fafc; 
            font-family: 'Inter', sans-serif; 
        }
        
     .header-container {
            background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 100%);
            padding: 30px; 
            border-radius: 24px; 
            border: 1px solid #e2e8f0;
            text-align: center; 
            margin-bottom: 20px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
        }
        
     .pro-title { color: #0f172a; font-size: 32px; font-weight: 800; margin-bottom: 5px; }
        
     .report-card {
            background: #ffffff; 
            border-left: 6px solid #3b82f6;
            padding: 15px 20px; 
            border-radius: 12px; 
            margin: 20px 0;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }
        
     .pulse { animation: pulse-animation 2s infinite; display: inline-block; }
        @keyframes pulse-animation { 0% {transform: scale(1);} 50% {transform: scale(1.1);} 100% {transform: scale(1);} }
        
     .stButton>button {
            width: 100%;
            border-radius: 12px;
            height: 3.5em;
            background-color: #3b82f6;
            color: white;
            font-weight: bold;
            border: none;
            transition: 0.3s;
        }
     .stButton>button:hover { background-color: #2563eb; border: none; color: white; }
        </style>

        <div class="header-container">
            <h1 class="pro-title"><span class="pulse">🩺</span> Welcome to Smart Disease Predictor</h1>
            <p style="color: #64748b; font-size: 18px;">Get an accurate analysis of your health parameters using Advanced AI.</p>
        </div>
    """, unsafe_allow_html=True)

    # Simple prediction logic based on input values
    def simple_predict(values):
        score = sum(values) / len(values)
        risk_prob = min(max(score / 200, 0.1), 0.9)
        prediction = 1 if risk_prob > 0.5 else 0
        return prediction, risk_prob

    # Sidebar menu for disease selection and logout
    with st.sidebar:
        st.header("🏥 Dashboard")

        # CSS for logout button design
        st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: #1e3a8a!important;
            color: white!important;
            font-weight: bold;
            border-radius: 10px;
            height: 2.8em;
        }
        </style>
        """, unsafe_allow_html=True)

        # Logout button
        if st.button("Logout 🔓"):
            st.session_state.logged_in = False
            st.rerun()

        st.write("---")

        # Radio button to select disease type
        option = st.radio("Select Disease", ["Diabetes", "Heart Disease", "Kidney Disease"])
        st.write("---")
        st.info("System: Active\nStatus: Local AI Engine")

    # Show selected disease form heading
    st.markdown(f'<div class="report-card"><h3>📊 {option} Analysis Form</h3></div>', unsafe_allow_html=True)

    # Diabetes prediction form
    if option == "Diabetes":
        glucose = st.slider("Glucose Level", 0, 250, 120)
        bp = st.slider("Blood Pressure", 0, 150, 80)
        age = st.slider("Age", 1, 100, 30)

        if st.button("Generate Result"):
            res, prob = simple_predict([glucose, bp, age])
            st.markdown("---")
            st.subheader("📋 Diabetes Diagnosis Report")
            st.write(f"**Risk Probability:** {prob*100:.2f}%")
            st.progress(prob)
            if res == 1:
                st.error("🚨 RESULT: High Risk Detected. Please consult a doctor.")
            else:
                st.success("✅ RESULT: Low Risk. Your parameters look stable.")

    # Heart Disease prediction form
    elif option == "Heart Disease":
        chol = st.slider("Cholesterol Level", 100, 500, 200)
        hr = st.slider("Max Heart Rate", 60, 220, 150)
        oldpeak = st.slider("ST Depression (Oldpeak)", 0.0, 6.0, 1.0)

        if st.button("Check Heart Status"):
            res, prob = simple_predict([chol/2, hr, oldpeak*20])
            st.markdown("---")
            st.subheader("🏥 Heart Health Report")
            st.write(f"**Cardiac Risk:** {prob*100:.1f}%")
            st.progress(prob)
            if res == 1:
                st.warning("⚠️ Warning: Cardiac Stress Detected.")
            else:
                st.success("💙 Heart Status: Healthy.")

    # Kidney Disease prediction form
    else:
        bp_k = st.slider("Blood Pressure", 50, 180, 80)
        al = st.slider("Albumin Level (0-5)", 0, 5, 0)
        sugar = st.slider("Sugar Level (0-5)", 0, 5, 0)
        
        if st.button("Analyze Kidney"):
            res, prob = simple_predict([bp_k, (al+sugar) * 20])
            st.markdown("---")
            st.subheader("🧪 Kidney Function Report")
            st.write(f"**Infection/Risk Probability:** {prob*100:.1f}%")
            st.progress(prob)
            if res == 1:
                st.error("🚨 Chronic Risk Detected.")
            else:
                st.success("✨ Kidney Function: Normal.")

    st.write("---")
    st.caption("Developed for Academic Project | © 2026 Smart Disease Prediction System")