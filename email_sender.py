import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    sender = input("Enter your Gmail: ")
    app_password = input("Enter your app password: ")
    receiver = input("Enter recipient email: ")
    subject = input("Enter subject: ")
    body = input("Enter message: ")

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, app_password)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()

    print("Email sent successfully!")
