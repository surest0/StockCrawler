import crawl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

stocks = crawl.get_top_10_stocks()

sender = ""
receiver = ""
password = ""


msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = "Today's stock"
body = "\n".join([f"{name}: {url}" for name, url in stocks])
msg.attach(MIMEText(body, 'plain'))

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)

