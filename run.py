from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    print(123)
    return "test page"


if __name__ == '__main__':
    app.run(debug=True)
