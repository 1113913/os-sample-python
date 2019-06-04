from flask import Flask
import sys

application = Flask(__name__)

@application.route("/fire")
def log():
    sys.stdout.write("ERROR\n")
    sys.stdout.flush()
    return "Firing the policy .."

@application.route("/")
def hello():
    return "Hello World !"

if __name__ == "__main__":
    application.run()
