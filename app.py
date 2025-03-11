from flask import Flask
import os
import subprocess
import pytz
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome! Visit <a href='/htop'>/htop</a> for system info.</h1>"

@app.route("/htop")
def htop():
    full_name = "Jugalkishor"
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"
    ist = pytz.timezone("Asia/Kolkata")
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S IST")
    try:
        top_output = subprocess.getoutput("top -b -n 1 | head -20")
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"
    
    return f"""
    <html>
    <head><title>HTop Output</title></head>
    <body>
        <h1>System Information</h1>
        <p><b>Name:</b> {full_name}</p>
        <p><b>Username:</b> {username}</p>
        <p><b>Server Time (IST):</b> {server_time}</p>
        <h2>Top Output</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
