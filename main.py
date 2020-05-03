from flask import Flask
from flask import jsonify


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/name/<value>')  # take some value
def name(value):
    val = {"value": value}
    return jsonify(val)  # return url, use val and not value

@app.route('/bob')  # take some value
def bob():
    val = {"value": "bob"}
    return jsonify(val)  # return "bob"

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]