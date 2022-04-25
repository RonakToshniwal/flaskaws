
from datetime import datetime
import database
from crypt import methods
from flask import Flask,redirect, render_template, request,url_for

from bucket import addBucket
app = Flask(__name__,template_folder='Template')
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/add")
def add():
    return render_template('add.html') 

@app.route("/delete/<id>")
def delete(id):
    database.delete(id)
    return redirect (url_for('show'))

@app.route("/edit/<id>")
def edit(id):
    user=database.findone(id)
    print(user)

    return render_template('edit.html',user=user)

@app.route("/editthis/<id>",methods=["POST"])

def editthis(id):

    from datetime import date
    user=request.form
    print(user)
    database.update(id,user['name'],user['roll'],datetime.now())
    return redirect (url_for('show'))


@app.route("/show")
def show():
    rows=database.show()
    for row in rows:
        print( row)
    return render_template('show.html',rows=rows)  

@app.route("/addthis",methods=['POST','GET'])
def addthis():
    user=request.form
    database.insert(user['name'],user['location'],datetime.now())
    print('added')
    addBucket(user['name'],user['location'])
    return redirect (url_for('home'))

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)