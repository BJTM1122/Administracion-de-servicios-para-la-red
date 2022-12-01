import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '
# Define params
rrdpath = '/home/jeovanny/PycharmProjects/Introduccion_SNMP/03-Practica3/RRD/'
imgpath = '/home/jeovanny/PycharmProjects/Introduccion_SNMP/03-Practica3/IMG/'
fname = 'trend.rrd'

mailsender = "bj.tmartinez1122@gmail.com"
mailreceip = "brayam.torresgi@gmail.com"
mailserver = 'smtp.gmail.com: 587'
password = '(Mariaantonieta11)'

def send_alert_attached(subject,servicio):
    """ Envía un correo electrónico adjuntando la imagen en IMG
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip
    fp = open(imgpath+servicio, 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    s = smtplib.SMTP(mailserver)

    s.starttls()
    # Login Credentials for sending the mail
    s.login(mailsender, password)

    s.sendmail(mailsender, mailreceip, msg.as_string())
    s.quit()