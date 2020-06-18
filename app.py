from flask import Flask, jsonify
import os, binascii
from backports.pbkdf2 import pbkdf2_hmac

app = Flask(__name__)

@app.route('/generateid/<name>')
def generateid(name):
    passwd = name.encode("utf8")
    key = pbkdf2_hmac("sha256", passwd, passwd, 50000, 8)
    return jsonify({'id': binascii.b2a_hex(key).decode("utf-8")})

if __name__ == '__main__':
    app.run()