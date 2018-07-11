from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:////home/shivam/blood/B-Positive/database.db')
app = Flask(__name__)
api = Api(app)

class City(Resource):
  def get(self,name,bg):
      if(bg=='AB+'):
          conn = db_connect.connect() # connect to database
          query = conn.execute("select * from product where city=:name",name)# This line performs query and returns json result
          return {'users': [i for i in query.cursor.fetchall()]} # Fetches all columns
      elif(bg=='AB-'):
          conn = db_connect.connect() # connect to database
          query = conn.execute("select * from product where city=:name and blood_group in ('AB-','A-','B-','O-')",name)
          return {'users': [i for i in query.cursor.fetchall()]} # Fetches all columns
      elif(bg=='B-'):
          conn = db_connect.connect() # connect to database
          query = conn.execute("select * from product where city=:name and blood_group in ('O-','B-')" ,name )
          return {'users': [i for i in query.cursor.fetchall()]} # Fetches all columns
      elif(bg=='O+'):
          conn = db_connect.connect() # connect to database
          query = conn.execute("select * from product where city=:name and blood_group in ('O-','O+')",name )
          return {'users': [i for i in query.cursor.fetchall()]} # Fetches all columns
      elif(bg=='B+'):
          conn = db_connect.connect() # connect to database
          query = conn.execute("select * from product where city=:name and blood_group in ('B+','B-','O-','O+') ",name )# This line performs query and returns json result
          return {'users': [i for i in query.cursor.fetchall()]} # Fetches all columns
      elif(bg=='O-'):
          conn = db_connect.connect() # connect to database
          query = conn.execute("select * from product where city=:name AND blood_group='O-'",name)# This line performs query and returns json result
          return {'users': [i for i in query.cursor.fetchall()]} # Fetches all columns
      elif(bg=='A+'):
          conn = db_connect.connect() # connect to database
          query = conn.execute("select * from product where city=:name AND blood_group in ('A+','A-','O-','O+')",name )# This line performs query and returns json result
          return {'users': [i for i in query.cursor.fetchall()]} # Fetches all columns
      else:
          conn = db_connect.connect()
          query = conn.execute("select * from product where city=:name and blood_group in ('A-','O-')",name )# This line performs query and returns json result
          return {'users': [i for i in query.cursor.fetchall()]} # Fetches all columns

api.add_resource(City, '/<string:name>/<string:bg>') # Route_1


if __name__ == '__main__':
   app.run(debug=True)
