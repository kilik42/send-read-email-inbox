import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'test@gmail.com'
password = 'letsgetitstarted2020'


def send_mail(text='Email Body', subject ='Hello world', from_email='test@gmail.com', to_emails=None):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = to_emails


    #log in to smtp server
    server = smtplib.SMTP(host='smtp.sendgrid.com', port=547)
    server.ehlo()
    server.starttls()
    server.login()
    server.sendmail(from_email, to_emails, msg_str)

    server.login(username, password)
    server.quit()

