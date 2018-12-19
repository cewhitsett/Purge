import facebook
import config
from flask import Flask, redirect, url_for, session, request
from flask_oauth import OAuth

secret_key = "development"
app_secret = "1e71589fa8a8539b374004befd843978"
app_id     = "352496362229395"

app = Flask(__name__)



if __name__ == "__main__":
    app.secret_key
    app.debug = True

