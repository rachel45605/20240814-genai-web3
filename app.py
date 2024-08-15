from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("Index.html")

if __name__ == "__main__":
    app.run(debug=True)
