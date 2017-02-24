import smtplib
import config
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.MIMEText import MIMEText
 
 
def send(subject, message):
    send_to(config.SEND_TO, subject, message)


def send_to(to, subject, message):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['To'] = to
    msg['From'] = 'HNews Alert <' + str(config.SENDER_EMAIL) + '>'
    
    part = MIMEText('text', "html")
    part.set_payload(message)
    msg.attach(part)
    
    session = smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT)
 
    session.ehlo()
    session.starttls()
    session.ehlo
    
    session.login(config.SENDER_EMAIL, config.SENDER_PASSWORD)

    qwertyuiop = msg.as_string()

    session.sendmail(config.SENDER_EMAIL, to.split(","), qwertyuiop)
    
    session.quit()
