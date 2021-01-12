import mysql.connector
import pandas as pd

db = mysql.connector.connect(user='root', password='password', host='localhost', database='ir_assignment')
cursor = db.cursor()

ratings = pd.read_csv('BX-Book-Ratings.csv', sep=";", encoding='ISO-8859-1')
books = pd.read_csv('BX-Books.csv', sep=";", encoding='ISO-8859-1')
for index, row in books.iterrows():
    if type(row[3]) != int:
        print(type(row[3]), row[3], index)

'''
for index, row in ratings.iterrows():
    if row['ISBN'][0] == "'":
        query = "INSERT INTO ratings VALUES (" + str(row['User-ID']) + ", " + str(row['ISBN']) + ", " + \
                str(row['Book-Rating']) + ");"
    else:
        query = "INSERT INTO ratings VALUES (" + str(row['User-ID']) + ", '" + str(row['ISBN']) + "', " + \
                str(row['Book-Rating']) + ");"

    try:
        cursor.execute(query)
    except Exception as e:
        print(e)
        print(row)
        print(index)
        print(query)
        input()
    if index % 1000 == 0:
        print(index)

db.commit()
'''