from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def welcome():

    return "<h1>Welcome</h1>"

@app.route("/contact")
def ContactPage():

    return render_template("contact.html")

@app.route("/home")
def Home():

    return "This is Home page"

@app.route("/gallery")
def gallery():

    return "This is Gallery"

if __name__ == "__main__":

    app.run(debug=True)