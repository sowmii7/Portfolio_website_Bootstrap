from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("about.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/experiments")
def experiments():
    return render_template("experiments.html")

@app.route("/article")
def article():
    return render_template("article.html")

if __name__ == "__main__":
    app.run(debug=True)

