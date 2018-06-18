from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return '''
    <html>
    <head><title>This is my flask app</title></head>
    </body>
    '''

if __name__ == "__main__":
    app.run(debug=True)

