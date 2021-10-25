import sqlite3
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as dates

from dateutil import parser



import plotly.graph_objs as go
import csv
con = sqlite3.connect("newdb.db")
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


#cur.execute("create view v_notprocessed as select indexData.Indexes, indexData.Open from indexData left join infoProcessed on infoProcessed.Indexes=indexData.Indexes and infoProcessed.Date=indexData.Date where infoProcessed.Date is null;")
#cur.execute("create view v_processed as select indexData.Date, indexData.Indexes, indexData.Open, indexData.Low, indexInfo.Exchange, indexInfo.Currency from indexData left join indexInfo on indexData.Indexes = indexInfo.Indexes group by indexData.Date")

first_graph = cur.execute("select Open, Date from v_processed where Indexes = 'N225' limit 20")
Open = []
Date = []
for row in first_graph:
    Open.append(row[0])
    Date.append(parser.parse(row[1]))


fig, ax = plt.subplots()


delta = datetime.timedelta(days=30)

fig.autofmt_xdate()
plt.title('figure 1', fontweight ="bold")
ax.plot_date(Date,Open,'-')
ax.xaxis.set_major_formatter(dates.DateFormatter('%Y-%m'))
plt.show()

second_graph = cur.execute("select Low, Date from v_processed where Indexes = 'N225' limit 20")

Low = []
Date = []
for row in first_graph:
    Low.append(row[0])
    Date.append(parser.parse(row[1]))


fig, ax = plt.subplots()
ax.plot_date(Date,Low,'-')
ax.xaxis.set_major_formatter(dates.DateFormatter('%Y-%m'))
fig.autofmt_xdate()
plt.title('figure 2', fontweight ="bold")
plt.show()

con.commit()
con.close()