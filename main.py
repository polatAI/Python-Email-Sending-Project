import json
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def sender(subject, message, from_email, to_email, login_pwd):
    msg = MIMEMultipart()

    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    body = message

    img_file = os.path.join('image', 'image.png')

    with open(img_file, "rb") as file:
        attach_img = MIMEApplication(file.read(), _subtype='png')

    attach_img.add_header('Content-Disposition', 'attachment', filename='image.png')

    msg.attach(MIMEText(body, 'plain'))
    msg.attach(attach_img)

    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(from_email, login_pwd)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

if __name__ == '__main__':
    with open('config.json', encoding='UTF-8') as file:
        config = json.load(file)

    sender_mail = config["sender_email"]
    sender_pwd = config["sender_pwd"]

    sender("Test Mail", "Bir yıldız bırakın :)", sender_mail, "to@test.com", sender_pwd)
