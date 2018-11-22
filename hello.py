from flask import Flask
from flask import render_template
from flask import make_response
from flask_script import Manager

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


"""
模板
"""


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


"""
cookie
"""


@app.route('/cookie')
def index():
    resp = make_response(render_template('hello.html'))
    resp.set_cookie('username', 'the username')
    return resp


if __name__ == '__main__':
    # app.run(host='0.0.0.0') # allow from other host
    app.run()

