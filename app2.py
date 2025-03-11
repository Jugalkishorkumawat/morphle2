# Import necessary libraries
from flask import Flask  # Flask framework for creating the web app
import os  # For accessing system environment variables
import subprocess  # For executing shell commands to get system process details
import pytz  # For handling time zones
from datetime import datetime  # For working with date and time

# Initialize the Flask application
app = Flask(__name__)

# Define the /htop endpoint
@app.route("/htop")
def htop():
    # Set your full name
    full_name = "Keshav"

    # Get the system username (compatible with both Windows and Linux)
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"

    # Get the current server time in IST (Indian Standard Time)
    ist = pytz.timezone("Asia/Kolkata")  # Define the IST timezone
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S IST")  # Format the date and time

    # Try to get the process list using 'top' (Linux) or 'tasklist' (Windows)
    try:
        if os.name == 'nt':  # Check if the operating system is Windows
            top_output = subprocess.getoutput("tasklist | findstr .")  # Windows command to list processes
        else:  # If it's a Unix-based system (Linux/macOS)
            top_output = subprocess.getoutput("top -b -n 1 | head -20")  # Linux command to get top 20 processes
    except Exception as e:
        # Handle any error while fetching the process list
        top_output = f"Error fetching process list: {str(e)}"
    
    # Return an HTML response to display system information and process list
    return f"""
    <html>
    <head>
        <title>HTop Output</title>  <!-- Page title -->
    </head>
    <body>
        <h1>System Information</h1>
        <p><b>Name:</b> {full_name}</p>  <!-- Display full name -->
        <p><b>Username:</b> {username}</p>  <!-- Display system username -->
        <p><b>Server Time (IST):</b> {server_time}</p>  <!-- Show current time in IST -->
        <h2>Process Output</h2>
        <pre>{top_output}</pre>  <!-- Display top process list -->
    </body>
    </html>
    """

# Start the Flask server when the script is run
if __name__ == "__main__":
    # Run the app on host 0.0.0.0 (publicly accessible) at port 8080
    # Debug mode is enabled for development purposes
    app.run(host="0.0.0.0", port=8080, debug=True)
