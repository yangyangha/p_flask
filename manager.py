from flask_script import Manager
from flask import Flask
from flask_script import Server

app = Flask(__name__)
manager = Manager(app)


# @manager.command
# def hello():
#     print("hello")

"""
https://flask-script.readthedocs.io/en/latest/
"""
"""
python3 manager.py hello -a=Joe  /python3 manager.py hello -a Joe

or
python3 manager.py hello --age=Joe / python3 manager.py hello --age Joe
取第一个字母
The short form -n is formed from the first letter of the argument, so “age” > “-a”. 
"""
"""
添加command 方法
1.decorator
2.add method
"""


@manager.command
def hello(age="Fred"):
    print("hello", age)


@app.route("/")
def hello():
    print("hello")
    return "hello G"


# server = Server(host="0.0.0.0", port=9000)
manager.add_command("runserver", Server())


if __name__ == '__main__':
    manager.run()