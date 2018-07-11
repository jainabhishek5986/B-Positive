from flask import Flask, request, jsonify,render_template,json
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
import json
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////home/shivam/blood/B-Positive/database.db'
db=SQLAlchemy(app)


@app.route("/")
def hello():
      return "Hello, World!"
      # /api/1.0/product
      # /api/1.0/product?city=Pune&bg=AB+
@app.route("/api/1.0/product",methods=['GET','POST','PUT'])
def act():
    if (request.method=='POST'):
        names=request.json['name']
        blood_groups=request.json['blood_group']
        addresss=request.json['address']
        citys=request.json['city']
        how_oftens=request.json['how_often']
        contacts=request.json['contact']
        email_ids=request.json['email_id']
        entry=Product(name=names,blood_group=blood_groups,address=addresss,
                        how_often=how_oftens,contact=contacts,email_id=email_ids)
        db.session.add(entry)
        db.session.commit()
        query = Product.query.get(12)
        return jsonify(query.custom_to_dict())

    elif request.method=='GET':
        citys=request.args.get("city")
        blood_group=request.args.get("blood_group")
        print(blood_group)
        print(citys)
        return str(Product.query.filter_by(city=citys))
        return "helo"
class Product(db.Model):
    id=db.Column(db.Integer,nullable=False,primary_key=True,autoincrement=True)
    name=db.Column(db.String(100),nullable=False)
    blood_group=db.Column(db.String(100),nullable=False)
    address=db.Column(db.String(100),nullable=True)
    city=db.Column(db.String(100),nullable=False)
    how_often=db.Column(db.Integer,nullable=False)
    #last_donate=db.Column(db.String(100),nullable=False)
    contact=db.Column(db.String(100),nullable=False)
    email_id=db.Column(db.String(30),nullable=False)
    def __repr__(self):
        return '<Product %r>' %self.contact
    def custom_to_dict(self):
        fields = [ 'name','blood_group','city','address','contact','email_id']
        return {item:self.__getattribute__(item) for item in fields}



if __name__ == "__main__":
    app.run(debug=True)
