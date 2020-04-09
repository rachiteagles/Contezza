from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from email.message import EmailMessage
import smtplib

app = Flask(__name__)
CORS(app)
api = Api(app)

class Rest_cont(Resource):
    def get(self):
        return {'abput':'hello'}

    def post(self):
        json = request.get_json()
              
        to = json['email']
        From = 'richa@contezzaconsultants.com'
        server = smtplib.SMTP_SSL('mail.contezzaconsultants.com',465)
        server.ehlo()
        #server.starttls()
        server.login('conteyf9','Manu@@2008')
        
        email_to = EmailMessage()
        body_to = "Thanks for contacting. We will get back to you soon"  
        email_to.set_content(body_to,subtype="html")
        
        email_to['From'] = From
        email_to['To'] = to
        email_to['Subject'] = "Contezza Consultants"
        server.send_message(email_to)
        
        email_from = EmailMessage()
        body_from = json['text']
        email_from.set_content(body_from,subtype="html")
        
        email_from['From'] = From
        email_from['To'] = From
        email_from['Subject'] = "Query from: "+json['name']+" number: "+json['number']+" email: "+json['email']
        server.send_message(email_from)
        
        server.quit()
        return json

api.add_resource(Rest_cont,'/')

if __name__ == '__main__':
    app.run(debug=True)
