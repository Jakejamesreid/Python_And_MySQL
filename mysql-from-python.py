import os
import pymysql
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
if os.path.exists(__location__+"\\env.py"):
    import env

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
dbuser = os.environ.get("DBUSER")
dbpass = os.environ.get("DBPASS")

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=dbuser,
                             password=dbpass,
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()