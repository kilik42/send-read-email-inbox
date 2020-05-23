import smtplib

username = 'test@gmail.com'
password = 'letsgetitstarted2020'


def send_mail(text='Email Body', subject ='Hello world', from_email='test@gmail.com', to_emails=None):
    assert isinstance(to_emails, list)

    #log in to smtp server
    server = smtplib.SMTP()
    server.ehlo()
    server.starttls()
    server.login()
    server.sendmail(from_email, to_emails, msg_str)

    server.login(username, password)
    server.quit()

