from flask import Flask, render_template, redirect, url_for, request
import sqlite3 as sql
from flask_paginate import Pagination
app=Flask(__name__)
@app.route('/')
def index(limit=10):
    con=sql.connect('human.db')
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute('Select * from user')
    data=cur.fetchall()
    page=int(request.args.get('page',1))
    start=(page-1)*limit
    paginate=Pagination(page=page,per_page=limit,total=len(data), css_framework="bootstrap4")
    cur.execute(f'Select * from user LIMIT {start},{limit}')
    paged_data=cur.fetchall()
    return render_template('index.html',users=paged_data,paginate=paginate)
@app.route('/daraalal')
def daraalal(limit=10):
    con=sql.connect('human.db')
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute('Select * from user')
    data=cur.fetchall()
    page=int(request.args.get('page',1))
    start=(page-1)*limit
    paginate=Pagination(page=page,per_page=limit,total=len(data), css_framework="bootstrap4")
    cur.execute(f'Select * from user ORDER BY name asc LIMIT {start},{limit}')
    paged_data=cur.fetchall()
    return render_template('index.html',users=paged_data,paginate=paginate)
@app.route('/esreg')
def esreg(limit=10):
    con=sql.connect('human.db')
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute('Select * from user')
    data=cur.fetchall()
    page=int(request.args.get('page',1))
    start=(page-1)*limit
    paginate=Pagination(page=page,per_page=limit,total=len(data), css_framework="bootstrap4")
    cur.execute(f'Select * from user ORDER BY name desc LIMIT {start},{limit}')
    paged_data=cur.fetchall()
    return render_template('index.html',users=paged_data,paginate=paginate)
if __name__=="__main__":
    app.run(debug=True)


