import os
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", page_title="Home")


@app.route("/about")
def about():
    data = []
    with open("data/squad.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", squads=data)


@app.route("/about/<slug>")
def about_squad(slug):
    squad_member = {}
    with open("data/squad.json", "r") as json_data:
        squad = json.load(json_data)
        for member in squad:
            if member["url"] == slug:
                squad_member = member
    return render_template("member.html", page_title=squad_member["name"], squad_member=squad_member)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
