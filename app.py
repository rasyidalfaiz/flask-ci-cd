from flask import Flask
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
DATABASE_URL = os.environ.get("DATABASE_URL")

@app.route("/")
def index():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        now = cur.fetchone()[0]
        cur.close()
        conn.close()
        return f"✅ Connected to database! Time: {now}"
    except Exception as e:
        return f"❌ Database error: {e}"
