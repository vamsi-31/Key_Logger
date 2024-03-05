
#Implemened KeyLogger

Keylogger and Process Monitor
This Python script offers functionalities for keylogging and monitoring processes on a system. It comprises two main parts:

Keylogger: Records keystrokes and sends the logged data via email.
Process Monitor: Monitors network activity and prompts the user to whitelist or blacklist suspicious processes.


## Installations
Python: Ensure you have Python installed on your system. You can download it from here.

Required Libraries: Install the necessary Python libraries using pip:

pip install pynput sendgrid psutil

SendGrid API Key: Obtain a SendGrid API key by signing up here. Replace 'YOUR_SENDGRID_API_KEY' with your actual API key in the script.

## Usage
Keylogger:
Run the script keylogger.py.
The keylogger will silently record keystrokes.
Press Enter to send the recorded data to the specified email address.
Press Esc to exit the keylogger.
Process Monitor:
Run the script process_monitor.py.
The monitor will continuously scan network activity.
When a suspicious process is detected, it will prompt you to whitelist or blacklist it.
Follow the on-screen instructions to manage processes.
Important Notes:
Email Configuration: Ensure the SMTP server used by SendGrid allows sending emails from the specified sender email address.
Security: Use this script responsibly. Do not use it for malicious purposes.
Whitelist and Blacklist: Manage the whitelist and blacklist carefully to avoid unintended consequences.
