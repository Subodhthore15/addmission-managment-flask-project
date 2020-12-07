
import mysql.connector

def connection():
    
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='@@subodh@@##',
        database ='admission'
        )
    print('suuces')
    return mydb

