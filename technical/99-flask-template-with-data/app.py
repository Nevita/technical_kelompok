from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/", )
def welcome_page():
    res = requests.get("https://api.github.com/users/nevita")
    gh_user = res.json()
    return render_template("welcome_page.html", user={'name': 'Nevita', 'username': 'nevita'}, gh_user=gh_user)


if __name__ == '__main__':
    app.run(debug=True)
