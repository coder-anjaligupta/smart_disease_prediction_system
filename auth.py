import sqlite3

def create_usertable():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, email TEXT, password TEXT)')
    conn.commit()
    conn.close()

def add_userdata(username, email, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO userstable VALUES (?,?,?)', (username, email, password))
    conn.commit()
    conn.close()

def login_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM userstable WHERE username=? AND password=?', (username, password))
    data = c.fetchall()
    conn.close()
    return data

def find_password(username, email):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT password FROM userstable WHERE username=? AND email=?', (username, email))
    data = c.fetchone()
    conn.close()
    return data