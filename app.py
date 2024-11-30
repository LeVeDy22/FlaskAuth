from flask import Flask, render_template, request
from models import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)


@app.route("/")
def main():
    return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)
