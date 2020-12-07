import pandas as pd
from connection import connection
from flask import Flask, request,  render_template,url_for,flash
import pickle

app = Flask(__name__)
app.config['SECRET_KEY']='subodhthore'
mydb=connection()



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_computer',methods=['GET','POST'])
def add_comp():
    
    if request.method=="POST":
        name=request.form.get('name')
        age=request.form.get('age')
        gender=request.form.get('gender')
        rollno=request.form.get('rollno')
        cor=mydb.cursor()
        query = '''INSERT INTO computer(name,age,gender,rollno)
           VALUES (%s,%s,%s,%s);
                 '''
        tu=(name,age,gender,rollno)
        cor.execute(query,tu)
        flash('Admission added successfully')
        mydb.commit()  
        
    return render_template('add_computer.html')



@app.route('/get_addmission_comp',methods=['GET','POST'])
def get_addmission_comp():
    cor=mydb.cursor()
    query='select * from computer;'
    cor.execute(query)
    result=cor.fetchall()
    return render_template('get_addmission_comp.html',result=result)
@app.route('/add_civil',methods=['GET','POST'])
def add_ci():
    if request.method=="POST":
        name=request.form.get('name')
        age=request.form.get('age')
        gender=request.form.get('gender')
        rollno=request.form.get('rollno')
        cor=mydb.cursor()
        query = '''INSERT INTO civil(name,age,gender,rollno)
           VALUES (%s,%s,%s,%s);
                 '''
        tu=(name,age,gender,rollno)
        cor.execute(query,tu)
        flash('Admission  added successfully')
        mydb.commit()
    return render_template('add_civil.html')

@app.route('/get_addmission_civil',methods=['GET','POST'])
def get_addmission_civil():
    cor=mydb.cursor()
    query='select * from civil;'
    cor.execute(query)
    result=cor.fetchall()
    return render_template('get_addmission_civil.html',result=result)

@app.route('/add_mechanical',methods=['GET','POST'])
def add_mech():
    if request.method=="POST":
        name=request.form.get('name')
        age=request.form.get('age')
        gender=request.form.get('gender')
        rollno=request.form.get('rollno')
        cor=mydb.cursor()
        query = '''INSERT INTO mechanical(name,age,gender,rollno)
           VALUES (%s,%s,%s,%s);
                 '''
        tu=(name,age,gender,rollno)
        cor.execute(query,tu)
        flash('Admission added successfully')
        mydb.commit()
    return render_template('add_mechanical.html')

@app.route('/get_addmission_mech',methods=['GET','POST'])
def get_addmission_mech():
    cor=mydb.cursor()
    query='select * from mechanical;'
    cor.execute(query)
    result=cor.fetchall()
    return render_template('get_addmission_mech.html',result=result)
if __name__ == "__main__":
    
    app.run()
    
    
    
    
    
    
    