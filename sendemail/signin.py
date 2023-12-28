import json
import random

from signedup import send, sending


def signindef():
    while True:
        user_email = input("Enter your email: ")
        with open('datas.json', 'r') as file:
            a = json.load(file)
        if user_email in a:
            passw = random.randint(1, 100)
            body = f'''<div style="width: 300px;
                                    height: 300px;
                                    background-color: #000;
                                    color: #fff;
                                    text-align: center;
                                    vertical-align: middle;
                                    display: flex;
                                    justify-content: center;
                                    align-items: center;">
                            <p style = "font-size: 100px;">{passw}</p>
                        </div>'''
            send('Code', 'bozorovshahob27@gmail.com', 'dapqtmlkkjfgljnb', user_email, body)
            enter = int(input("Enter the password which was sent: "))
            if enter == passw:
                sending(user_email, a[user_email])
                break
            else:
                print("It's wrong")
                break
        else:
            print("We can't find you")