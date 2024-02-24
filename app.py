from flask import Flask,render_template,request,redirect,url_for
#create flask app
app=Flask(__name__)

@app.route('/')
def home():
    return "<h2>hello world</h2>"

@app.route('/welcome')
def welcome():
    return "redirected to welcome page"

@app.route('/index')
def index():
    return render_template("index.html")  
#redirect to template html file in local ,it should be present in templates folder(name should be templates only)
#redirect to index html file 

@app.route('/success/<int:score>')
def success(score):
    return "PROMOTED The score is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "FAILED The score is "+str(score)

@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])      #give the names in the form in the input type
        science=float(request.form['science'])
        history=float(request.form['history'])
        average=(maths+science+history)/3
        res=""
    if average>50:
        res="success"
    else:
        res="fail"
    
    #return redirect(url_for(res,score=average))

    return render_template('result.html',results=average)  
    #there in results.html page we will be having results variable in {{}} this will receive the average variable.


if __name__=='__main__':
    app.run(debug=True)


