from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def hello_world():
    return 'Hello World by Olugbenga Ajayi using GitHub Actions ;)!'

# Run the app
if __name__ == '__main__':
    # Make the app externally visible (host='0.0.0.0') so that it works in Docker
    app.run(host='0.0.0.0', port=5000)
