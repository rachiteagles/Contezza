from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import smtplib

app = Flask(__name__)
CORS(app)
api = Api(app)

class Rest_cont(Resource):
    def get(self):
        return {'abput':'hello'}

    def post(self):
        json = request.get_json()
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login('rachit1405@gmail.com','heisenberg321')
        message= 'Subject: {}\n\n{}'.format('from:'+json['name']+' number:'+json['number'],json['text'])
        server.sendmail('rachit1405@gmail.com',json['email'],message)
        server.quit()
        return json

api.add_resource(Rest_cont,'/')

if __name__ == '__main__':
    app.run(debug=True)
