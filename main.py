from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render_the_map():
    return render_template("ina.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
