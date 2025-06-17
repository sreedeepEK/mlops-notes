from flask import Flask, render_template

#wsgi application
app = Flask(__name__) 

@app.route("/")
def welcome():
    return "Hello world!"
    
    
@app.route("/index")
def index():
    return "Welcome to the index page"

if __name__ == "__main__":
    app.run(debug=True)
    
    