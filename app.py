from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)


# Database connection
def get_connection():
    database_url = os.environ.get("DATABASE_URL")

# Database create
def create_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            service TEXT NOT NULL,
            appointment_time TEXT NOT NULL
        )
    """)

    conn.commit()
    cursor.close()
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

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO appointments
        (name, phone, service, appointment_time)
        VALUES (%s, %s, %s, %s)
    """, (name, phone, service, appointment_time))

    conn.commit()
    cursor.close()
    conn.close()

    return """
    <h2>Appointment booked successfully!</h2>
    <a href="/">Go back</a>
    """


# Create table when app starts
create_database()


if __name__ == "__main__":
    app.run(debug=True)
    

