from flask import Flask
from flask import request
import socket
import os
import sys
import requests

app = Flask(__name__)

@app.route('/service/<service_number>')
def hello(service_number):
    if int(os.environ['SERVICE_NAME']) == 2:
        app.logger.info(request.headers)

    return 'Hello from behind Envoy (service %s)! hostname: %s resolved hostname: %s' % (
        os.environ['SERVICE_NAME'], 
        socket.gethostname(), 
        socket.gethostbyname(socket.gethostname())
    )

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)