from flask import Flask
from flask import request
import socket
import os
import sys
import requests

app = Flask(__name__)

TRACE_HEADERS_TO_PROPAGATE = [
    'X-Ot-Span-Context',
    'X-Request-Id',

    # Zipkin headers
    'X-B3-TraceId',
    'X-B3-SpanId',
    'X-B3-ParentSpanId',
    'X-B3-Sampled',
    'X-B3-Flags',

    # Jaeger header (for native client)
    "uber-trace-id"
]

@app.route('/service/<service_number>')
def hello(service_number):
    return ('Hello from behind Envoy (service {})! hostname: {} resolved'
            'hostname: {}\n'.format(os.environ['SERVICE_NAME'], 
                                    socket.gethostname(),
                                    socket.gethostbyname(socket.gethostname())))

@app.route('/service/rule/test')
def rule_test():
    return socket.gethostbyname(socket.gethostname())

@app.route('/service/regex/<service_number>')
def regex_test(service_number):
    return socket.gethostbyname(socket.gethostname()), service_number

@app.route('/service/ratelimit/test')
def ratelimit_test():
    return socket.gethostbyname(socket.gethostname())

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
