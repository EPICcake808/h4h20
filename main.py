from flask import Flask, render_template, request, current_app


app = Flask(__name__)


@app.route('/')
def html():
    return current_app.send_static_file('temp.html')


if __name__ == '__test__':
    app.run()
