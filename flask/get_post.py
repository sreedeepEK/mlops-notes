from flask import Flask, render_template ,request

#wsgi application
app = Flask(__name__) 

@app.route("/")
def welcome():
    return "Hello world!"
    
    
@app.route("/index", methods = ['GET'])
def index():
    return "Welcome to the index page"

@app.route('/form', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        
        name = request.form['name']
        return f"Hello {name}!"
            
       
    return render_template('form.html') 


#variable rule
@app.route('/sucess/<score>')
def success(score):
    return "The marks got is " +score


if __name__ == "__main__":
    app.run(debug=True)
    
    