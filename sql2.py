from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

engine=create_engine('mysql://root:pass@localhost/flaskr')
Base=declarative_base()

class User(Base):
	__tablename__='users'
	id=Column(Integer,primary_key=True)
	name=Column(String(30))
	fullname=Column(String(50))
	password=Column(Stgring(50))

	def __init__(self,name,password):
		self.name=name
		self.password=password

