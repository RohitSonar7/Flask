from flask import Flask

app = Flask(__name__)

@app.route("/")
def Welcome():
    return "Welcome to my Website"
@app.route("/contact")
def contact():
    return "This is a contact page"
@app.route("/home")
def home():
    return "This is a Home page"
@app.route("/gallery")
def gallery():
    return "This is a Gallery page"


if __name__ == "__main__":
    app.run()