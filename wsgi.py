#!/usr/bin/env python


import time
import sys
import os
import json
from flask import Flask, Request, Response
application = app = Flask('wsgi')

@app.route('/')
def welcome():
    return 'welcome to appfog!'

if __name__ == '__main__':
    app.run(debug=True)
