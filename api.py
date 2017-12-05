#!/usr/bin/python

# description: apollo api, does this need anymore description
# main file in this folder
# editors: Ayat Amin, Vaughn Ganem Haka


''' Flask REST API for interfacing with Telematics and Leidos data
'''

from flask import Flask, request, jsonify, make_response
# from util import api_call_logger
import logging, sys

logging.basicConfig(level=logging.DEBUG)
app = Flask("apollo-api")

@app.route("/status", methods=['GET'])
# @api_call_logger
def status():
    return jsonify({"status": "success"})

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=8080)

    except Exception as e:
        logging.error(e)
        sys.exit(1)
    else:
        sys.exit(0)
