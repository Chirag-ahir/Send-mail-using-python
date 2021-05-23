import time
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gmail_user = "ahirchirag8125@gmail.com"
gmail_pwd = "180170111001"
FROM = ['ahirchirag8125@gmail.com']
TO = ['ahirchirag1459@gmail.com'] #must be a list

msg = MIMEMultipart()
time.sleep(1)
msg['Subject'] ="SECURITY"
body="Your Device at risk"
msg.attach(MIMEText(body,'plain'))
time.sleep(1)

fp = open("alert.png", 'rb')
time.sleep(1)
img = MIMEImage(fp.read())
time.sleep(1)
fp.close()
time.sleep(1)
msg.attach(img)
time.sleep(1)

try:
    server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
    print ("smtp.gmail")
    server.ehlo()
    print ("ehlo")
    server.starttls()
    print ("starttls")
    server.login(gmail_user, gmail_pwd)
    print ("reading mail & password")
    server.sendmail(FROM, TO, msg.as_string())
    print ("from",FROM)
    print("To",TO)
    server.close()
    print ('Mail has been sent successfully')
except:
    print ("failed to send mail")
