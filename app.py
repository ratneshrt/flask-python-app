import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

# Load DB connection info from environment variables
DB_HOST = os.getenv("POSTGRES_HOST", "db")
DB_NAME = os.getenv("POSTGRES_DB", "testdb")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "example")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "success",
        "message": "Flask app v2 running successfully!"
    }), 200

@app.route("/health", methods=["GET"])
def health_check():
    """Check DB connection and return result."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT,
            connect_timeout=3
        )
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        cur.close()
        conn.close()
        return jsonify({
            "status": "ok",
            "database": "connected"
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "database": "unreachable",
            "details": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
