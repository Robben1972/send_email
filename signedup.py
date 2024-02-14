import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL

msg = MIMEMultipart()


def send(title, email, password, to, body):
    msg['Subject'] = title
    msg['From'] = email
    msg['To'] = to
    msg.attach(MIMEText(body, 'html'))
    if to.endswith('gmail.com'):
        with SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email, password)
            smtp.sendmail(email, to, msg.as_string())
    elif to.endswith('icloud.com'):
        with SMTP_SSL('smtp.icloud.com', 465) as smtp:
            smtp.login(email, password)
            smtp.sendmail(email, to, msg.as_string())


def sending(email, password):
    while True:
        print('1. Send email')
        print('2. Exit')
        section_p = int(input("Choose: "))
        if section_p == 1:
            to = input("Who you want to send: ")
            title = input("Enter the title of email: ")
            body = input("Enter the text of email: ")
            send(title, email, password, to, body)
            print("Successfully sent")
        elif section_p == 2:
            break


def signedupdef():
    while True:
        user_email = input("Enter your email: ")
        user_password = input("Enter your password for access send email: ")

        with open('datas.json', 'r') as file:
            a = json.load(file)
            if user_email in a:
                print("We already have this account")
                file.close()
            else:
                file.close()
                if not user_email.endswith('@gmail.com'):
                    print("It's not email")
                else:
                    a[user_email] = user_password
                    with open('datas.json', 'w') as data:
                        json.dump(a, data, indent=4)
                    data.close()
                    sending(user_email, user_password)
        break


