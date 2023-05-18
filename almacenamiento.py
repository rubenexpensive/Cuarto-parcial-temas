import mysql.connector

conexio = mysql.connector.connect(user = 'root', password = '',host = '127.0.0.1')
cursor = conexio.cursor()
sql = "CREATE DATABASE IF NOR EXISTS TIENDA3"
cursor.execute(sql)
conexio.commit()
cursor.close()
conexio.close()


