from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hemlo contact me at telegram.me/pro_noober'


if __name__ == "__main__":
    app.run()
