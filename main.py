import sqlite3
import numpy as np
import pandas as pd
import csv
con = sqlite3.connect("loldb.db")
cur = con.cursor()
tables = cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
for table in (tables):
    print(table)

indexData = open("/Users/toleugazin/PycharmProjects/pythonProject3/indexData.csv")
indexInfo = open("/Users/toleugazin/PycharmProjects/pythonProject3/indexInfo.csv")
indexProcessed = open("/Users/toleugazin/PycharmProjects/pythonProject3/indexProcessed.csv")

rows = csv.reader(indexData)
rows1 = csv.reader(indexInfo)
rows2 = csv.reader(indexProcessed)

cur.executemany("INSERT OR IGNORE INTO indexData VALUES (?, ?, ?, ?, ?, ?, ?, ?)", rows)
cur.executemany("INSERT INTO indexInfo VALUES (?, ?, ?, ?)", rows1)
cur.executemany("INSERT OR IGNORE INTO infoProcessed VALUES (?,?, ?, ?, ?, ?, ?, ?, ?)", rows2)


cur.execute("SELECT indexData.Indexes, infoProcessed.CloseUSD FROM indexData LEFT JOIN infoProcessed ON indexData.Indexes = infoProcessed.Indexes")
print(cur.fetchall())
con.commit()