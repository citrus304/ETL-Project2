# Note: To create a server, we simply import Flask (#1),
#       and use it as a factory to create an app (#2).

# 1. import Flask
from flask import Flask

# 2. Create an app, being sure to pass __name__
# Note: For our purposes, passing __name__ to Flask is essentially mandatory.
#       Details: http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
# Note: We use @app.route to associate an endpoint/URL (/ or /about)
#       with the result of a function call (home or about, respectively).
@app.route("/")
def home():
    # Print message on server (e.g., for logging)
    print("Server received request for 'Home' page...")
    # Return result to client (print message on client)
    return "Welcome to my 'Home' page!"


# 4. Define what to do when a user hits the /about route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

# 5. Define main behavior
# Details: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    # Notes:
    # - app.run is all we need to do to start the development server
    # - passing debug=True makes development much easier
    # - but, in production, best practices demand debug=False always
    app.run(debug=True)

# Go to (in your browser):
# localhost:5000
# localhost:5000/about