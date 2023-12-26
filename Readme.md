# Keylogger with Email Reporting

This Python script implements a basic keylogger with email reporting functionality. It utilizes the pynput library for keyboard monitoring and smtplib for sending email reports.

## Usage

1. Run the script (`python keylogger.py`), and the keylogger will start recording key presses.
2. Press 'Esc' to stop the keylogger.
3. The recorded keystrokes are saved in a log file ('keylogger_log.txt').
4. An email report containing the log file is sent to a specified email address.

**Note:** This script is for educational purposes only, and using it without proper authorization is illegal.

## Dependencies
- [pynput](https://pypi.org/project/pynput/)

## Instructions

1. **Setting Up Email Credentials:**
   - Replace the empty strings (`""`) in the `log_file_path`, `sender_email`, `sender_password`, and `recipient_email` variables with your desired values.
   
2. **Configuring Email Server:**
   - The script is set up to use the SMTP server for Outlook. If you are using a different email provider, update the `smtp_server` and `smtp_port` accordingly in the `EmailHandler` class.

3. **Running the Keylogger:**
   - Execute the script, and the keylogger will start running in the background.

4. **Stopping the Keylogger:**
   - Press 'Esc' to stop the keylogger. The program will log the end time in the keylogger log file.

5. **Checking Logs:**
   - The recorded keystrokes are saved in the specified log file (`keylogger_log.txt`). You can review this file to see the captured data.

6. **Email Reporting:**
   - The keylogger is set to send email reports every 10 seconds (configurable in `time_interval`). The log file is attached to the email with the subject "Keylogger Report."

**Important:** Ensure that you have the necessary permissions to run this script, and only use it in accordance with applicable laws and regulations.

## Acknowledgments

This script was created for educational purposes and should only be used responsibly and ethically.
