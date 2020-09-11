import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(host='localhost',
    user='root',
    password='',
    db='testpython')

cursor = mydb.cursor()
data  = pd.read_csv (r'C:\Users\Gigabyte\Desktop\test.csv')  
df = pd.DataFrame(data, columns= ['name','phone','roll_no'])

for row in df.itertuples():
        mysql_query = "INSERT INTO students (roll_no,phone,name) VALUES (%s, %s, %s)"
        singleRow = (row.roll_no,row.phone,row.name)
        cursor.execute(mysql_query, singleRow)
mydb.commit()       

mydb.commit()
cursor.close()
print ("Done")
