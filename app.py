from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = psycopg2.connect(os.environ.get("DATABASE_URL"))
        cur = conn.cursor()
        cur.execute("SELECT 1")
        cur.fetchone()
        cur.close()
        conn.close()
        db_status = "Connected to PostgreSQL!"
    except Exception as e:
        db_status = f"Connection failed: {e}"

    return render_template("index.html", db_status=db_status)

if __name__ == "__main__":
    app.run(debug=True)
