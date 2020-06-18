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
        list_of_names = ['Fred', 'fred']
        # prepare a string with same number of placeholders as in list_of_names
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("delete from Friends where name in ({})"
                       .format(format_strings), list_of_names)
        connection.commit()
finally:
    # close connection to sql, regardless
    connection.close()
