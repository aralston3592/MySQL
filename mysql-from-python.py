import os
import pymysql

# get Username from Gitpod workspace
# (modify this variabke if running in other environment)
username = os.getenv('GITPOD_USER')

# Connect to db
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # run a query
    with connection.cursor() as cursor:
        sql = "select * from Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # close connection to sql, regardless
    connection.close()
