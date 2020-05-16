from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to deployed app updated to test!"



if __name__=="__main__":
    app.run(debug=True)
