import nltk
# nltk.download()
from engine import CONNECTION_STRING
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
import sqlalchemy
from sqlalchemy.orm import sessionmaker, session
from sqlalchemy.dialects.mysql import insert
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

engine = create_engine(CONNECTION_STRING, echo=True)
Base = declarative_base()
connection = engine.connect()
metadata = MetaData() #makes metadata in the table available in python

listings_table = Table('listings',  metadata, autoload=True, autoload_with=engine)
# print(engine.table_names()) #check avaialble tables from the scheme
# print(listings_table.columns.keys()) #check a tables columns

prod_names = []
#query all product names from product name column
prod_name_query = select([listings_table.columns.product_name])
prod_name_Proxy = connection.execute(prod_name_query)
product_name_results = prod_name_Proxy.fetchall()
print(type(product_name_results))
print(len(product_name_results))

new_names = str(product_name_results)
# x = [name.replace(")", "") for name in new_names]
# print(x)

#remove stopwords from product names
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(new_names)
filtered_sentence = [w for w in word_tokens if not w in stop_words]

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)

Ps = PorterStemmer()
for words in filtered_sentence:
    print(Ps.stem(words))



