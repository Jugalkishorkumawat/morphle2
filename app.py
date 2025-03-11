from flask import Flask  # Flask framework for creating the web app
import os  # For accessing system environment variables
import subprocess  # For executing shell commands
import pytz  # For handling time zones
from datetime import datetime  # For working with date and time

# Initialize the Flask app
app = Flask(__name__)

# Define the /htop endpoint
@app.route("/htop")
def htop():
    # Set your full name
    full_name = "Jugalkishor"

    # Get the system username (compatible with both Windows and Linux)
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"

    # Get the current server time in IST (Indian Standard Time)
    ist = pytz.timezone("Asia/Kolkata")
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S IST")

    # Try to get the process list using 'top' (Linux) or 'tasklist' (Windows)
    try:
        if os.name == 'nt':  # 'nt' = Windows
            top_output = subprocess.getoutput("tasklist | findstr .")  # Limited output for Windows
        else:  # For Linux and macOS
            top_output = subprocess.getoutput("top -b -n 1 | head -20")  # Unix-based command
    except Exception as e:
        # Handle any error while fetching the process list
        top_output = f"Error fetching process list: {str(e)}"
    
    # HTML response to display data on the webpage
    return f"""
    <html>
    <head>
        <title>HTop Output</title>
    </head>
    <body>
        <h1>System Information</h1>
        <p><b>Name:</b> {full_name}</p>
        <p><b>Username:</b> {username}</p>
        <p><b>Server Time (IST):</b> {server_time}</p>
        <h2>Process Output</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

# Start the Flask server
if __name__ == "__main__":
    # Run the app on host 0.0.0.0 (publicly accessible) at port 8080
    app.run(host="0.0.0.0", port=8080, debug=True)
