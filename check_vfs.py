import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

# URL to monitor (replace with actual VFS appointment page)
url = "https://visa.vfsglobal.com/ago/en/prt/book-an-appointment"

def check_appointments():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    if "No appointments available" not in soup.text:
        send_email("Appointments may be available! Check VFS site.")

def send_email(message):
    sender = "your_email@gmail.com"
    receiver = "ljnascy@gmail.com"
    password = "your_app_password"

    msg = MIMEText(message)
    msg["Subject"] = "VFS Portugal Appointment Alert"
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())

check_appointments()
