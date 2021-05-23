#this program provide security to device. if user try to login in account more than 3 times with wrong password then mail will automatically send to the owner. 

i=0
import time
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gmail_user = "****************"
gmail_pwd = "*************"
FROM = ['***************']
TO = ['***************'] #must be a list

def login():
    msg = MIMEMultipart()
    time.sleep(1)
    msg['Subject'] = "SECURITY"
    body = "Your Device is at risk"
    msg.attach(MIMEText(body, 'plain'))
    time.sleep(1)

    fp = open("alert.png", 'rb')
    time.sleep(1)
    img = MIMEImage(fp.read())
    time.sleep(1)
    fp.close()
    time.sleep(1)
    msg.attach(img)
    time.sleep(1)

    server = smtplib.SMTP("smtp.gmail.com", 587)  # or port 465 doesn't seem to work!
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pwd)
    server.sendmail(FROM, TO, msg.as_string())
    server.close()
    print('You exceeds your limit')
    print('Mail has been sent successfully')

for i in range(3):
    Password = "redmik20pro"
    password = input("Enter your password :")
    if password==Password:
        print("You login into your account successfully")
    else:
        i = i + 1
        if(i==3):
            login()
            break
        print("You entered wrong password. please enter correct password")






