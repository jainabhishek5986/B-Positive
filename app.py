from flask import Flask, request, jsonify,render_template
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////home/arti/blood/B-Positive/database.db'
db=SQLAlchemy(app)


@app.route("/")
def hello():
      return "Hello, World!"
@app.route("/product/<int:a>/",methods=['GET','POST'])
def pro(a):
    if request.method=='GET':
        return "Hello"

class Product(db.Model):
    id=db.Column(db.Integer,nullable=False,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    blood_group=db.Column(db.String(100),nullable=False)
    address=db.Column(db.String(100),nullable=True)
    city=db.Column(db.String(100),nullable=False)
    how_often=db.Column(db.Integer,nullable=False)
    contact=db.Column(db.String(100),primary_key=True)
    email_id=db.Column(db.String(30),unique=True,nullable=False)
    def __repr__(self):
        return '<Product %r>' %self.contact



if __name__ == "__main__":
    app.run(debug=True)
