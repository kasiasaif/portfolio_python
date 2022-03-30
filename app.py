
from flask import Flask, Blueprint, render_template, url_for, redirect



views = Blueprint(__name__, "views")

app = Flask(__name__)
app.register_blueprint(views, url_prefix = "/")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/kasia")
def kasia_page():
    return render_template("kasia.html", favorite_thing = "Coffee")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/experience")
def experience_page():
    return render_template("experience.html")

@app.route("/home")
def home_redirect():
    return redirect(url_for("home"))



@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404



if __name__ == "__main__":
    app.run(debug=True, port=8000)

########################################