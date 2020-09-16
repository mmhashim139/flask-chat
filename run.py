import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []


def add_messages(username, message):
    """ Add messages to the messages list"""
    now = datetime.now().strftime(" %H:%M:%S ")
    messages.append("({}): {}: {}".format(now, username, message))


def get_all_messages():
    """ Get all of the messages and seperate them with a br """
    return "<br>".join(messages)


@app.route("/", methods=["GET", "POST"])
def index():
    """ Main Page with Instructions """

    if request.method == "POST":
        session["username"] = request.form["username"]
    if "username" in session:
        return redirect(session["username"])

    return render_template("index.html")


@app.route("/<username>")
def user(username):
    """ Display chat messages """
    return "<h2>Welcome, {0} </h2>  {1}".format(username, get_all_messages())


@app.route("/<username>/<message>")
def send_message(username, message):
    """ Create a new message and redirect to the chat app"""
    add_messages(username, message)
    return redirect("/" + username)


app.run(host=os.getenv("IP"), port=os.getenv("PORT"), debug=True)
