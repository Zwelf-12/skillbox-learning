import sentry_sdk
from flask import Flask, request
sentry_sdk.init(
    dsn="https://e9318f5b96e488a94524397dd5f3d69d@o4507406755102720.ingest.de.sentry.io/4507406758051922",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)
app = Flask(__name__)


@app.route("/")
def hello_world():
    if request.args.get("error"):
        1/0 # raises an error
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=True)