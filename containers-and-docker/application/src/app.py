#!/usr/bin/env python3

from flask import Flask, request, redirect, url_for
import socket
import os


# create app (exported as a global for possible re-use)
app = Flask(__name__)


@app.route('/')
def hello_world():
   return 'Flask running in a container as {}!\n'.format(socket.gethostname())


@app.route('/crash')
def crash():
   os._exit(1)


if __name__ == '__main__':
   app.run(host='0.0.0.0') # listen on all interfaces, not just localhost
