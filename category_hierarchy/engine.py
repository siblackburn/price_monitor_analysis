from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text)

drivername="mysql"
user="root"
passwd="password"
host="127.0.0.1"
port="3306"
db_name="price_crawler_db"
CONNECTION_STRING = f'mysql+pymysql://{user}:{passwd}@{host}/{db_name}'

Base = declarative_base()


def db_connect():
    return create_engine(CONNECTION_STRING)

