from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 


@app.route('/')
def contador():
    if 'num' in session:
        session['num'] += 1
    else:
        session['num'] = 0
    
    return render_template("index.html")

@app.route('/destroy')
def eliminar():
    session.clear()
    return redirect('/')

@app.route('/add2')
def aumentar():
    session['num'] += 1
    return redirect('/')

if __name__ == "__main__": 
    app.run(debug=True)