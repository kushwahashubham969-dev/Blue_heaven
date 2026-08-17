from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


# Database create 
def create_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            service TEXT NOT NULL,
            appointment_time TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Form data 
@app.route("/book", methods=["POST"])
def book():

    name = request.form["name"]
    phone = request.form["phone"]
    service = request.form["service"]
    appointment_time = request.form["appointment_time"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO appointments
        (name, phone, service, appointment_time)
        VALUES (?, ?, ?, ?)
    """, (name, phone, service, appointment_time))

    conn.commit()
    conn.close()

    return """
    <h2>Appointment booked successfully!</h2>
    <a href="/">Go back</a>
    """


if __name__ == "__main__":
    create_database()
    app.run(debug=True)

if __name__ == "__main__":
    create_database()
    app.run(host="10.245.14.174", port=5000, debug=True)        

