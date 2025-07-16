import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import os

# URL to monitor (replace with your local VFS page if needed)
url = "https://visa.vfsglobal.com/ago/en/prt/book-an-appointment"

def check_appointments():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    if "No appointment slots are currently available" not in soup.text:
        send_email("✅ VFS Portugal: Appointments may be available! Check the site now.")
    else:
        print("No appointments available at the moment.")

def send_email(message):
    sender = "your_email@gmail.com"
    receiver = "ljnascy@gmail.com"
    password = os.environ.get("EMAIL_PASSWORD")

    msg = MIMEText(message)
    msg["Subject"] = "VFS Portugal Appointment Alert"
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())

check_appointments()
