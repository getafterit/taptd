from flask import Flask
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC5c2e24bba540815aa85b6aa52e9fbfa7'
auth_token = '9c9bd1fadb2f4b993a809fe06752d846'
client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
	
if __name__ == "__main__":
    app.run()