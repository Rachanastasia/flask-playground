from my_flask import app


@app.route('/')
def index():
    return 'Hello World!'
