
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='from_ouremail@example.com',
    to_emails='to@example.com',
    subject='Welcome to our website',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('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'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
