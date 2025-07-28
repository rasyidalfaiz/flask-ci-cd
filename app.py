from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def hello():
    conn = psycopg2.connect(os.environ.get("DATABASE_URL"))
    cur = conn.cursor()
    cur.execute("SELECT NOW()")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return f"Connected to DB! Current time: {result[0]}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
