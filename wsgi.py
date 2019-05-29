from flask import Flask
application = Flask(__name__)

@application.route("/log")
def log():
    print("TEST LOG")
    return "Test Log"

@application.route("/")
def hello():
    return "Hello World !"

if __name__ == "__main__":
    application.run()
