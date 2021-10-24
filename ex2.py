
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mysql.connector import connect, Error
import mysql.connector as mysql
from sqlalchemy import create_engine, types

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "rxeo4on4",
    database = "New_schema"
)

cursor = db.cursor()

cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

for table in (tables):
    print(table)

#engine = create_engine("mysql://{root}:{rxeo4on4}@localhost/{New_schema}")

indexData = pd.read_csv("/Users/toleugazin/PycharmProjects/pythonProject3/indexData.csv")
df = pd.DataFrame(indexData, columns= ['Index', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj close', 'Volume'])
indexInfo = pd.read_csv("/Users/toleugazin/PycharmProjects/pythonProject3/indexInfo.csv")
indexProcessed = pd.read_csv("/Users/toleugazin/PycharmProjects/pythonProject3/indexProcessed.csv")
print(indexData.dtypes)
print(indexInfo.dtypes)
print(indexProcessed.dtypes)

#indexData.to_sql("index_data", con = engine, if_exists = 'append', chunksize = 1000,index=False)

for row in df.itertuples():
    cursor.execute('''
                INSERT INTO New_schema.index_data(Index, Date, Open, High, Low, Close, Volume)
                VALUES (%s,%s,%s,%s,%s,%s)
                ''',
                row.Index,
                row.Date,
                row.Open,
                row.High,
                row.Low,
                row.Close,
                row.Volume
               )

cursor.execute("SELECT * FROM index_data")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mysql.connector import connect, Error
import mysql.connector as mysql
from sqlalchemy import create_engine, types

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "rxeo4on4",
    database = "New_schema"
)

cursor = db.cursor()

cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

for table in (tables):
    print(table)

#engine = create_engine("mysql://{root}:{rxeo4on4}@localhost/{New_schema}")

indexData = pd.read_csv("/Users/toleugazin/PycharmProjects/pythonProject3/indexData.csv")
df = pd.DataFrame(indexData, columns= ['Index', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj close', 'Volume'])
indexInfo = pd.read_csv("/Users/toleugazin/PycharmProjects/pythonProject3/indexInfo.csv")
indexProcessed = pd.read_csv("/Users/toleugazin/PycharmProjects/pythonProject3/indexProcessed.csv")
print(indexData.dtypes)
print(indexInfo.dtypes)
print(indexProcessed.dtypes)

#indexData.to_sql("index_data", con = engine, if_exists = 'append', chunksize = 1000,index=False)

for row in df.itertuples():
    cursor.execute('''
                INSERT INTO New_schema.index_data(Index, Date, Open, High, Low, Close, Volume)
                VALUES (%s,%s,%s,%s,%s,%s)
                ''',
                row.Index,
                row.Date,
                row.Open,
                row.High,
                row.Low,
                row.Close,
                row.Volume
               )

cursor.execute("SELECT * FROM index_data")
