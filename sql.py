from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

engine=create_engine('mysql://root:pass@localhost/flaskr')
Base=declarative_base()
