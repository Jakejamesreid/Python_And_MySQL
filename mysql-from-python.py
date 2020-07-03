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

#Cursors are used to execute database queries. To open a cursor and execute a query, use the following code
try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()

# The fetchall() method can be used to obtain all the results for the query. The results will not be easily readable so to get them line by line in loop over the cursor object and print each line. The result will be returned as a tuple
try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()

# To return the results as a dict you can pass pymysql.cursors.DictCursor when creating the cursor
try:
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)
        for row in cursor:
            print(row)
finally:
    connection.close()

# There are also uncached cursors which are read one line at a time and are better for saving space

# To create a new table
try:
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS Friends(name char(20), age int, DOB datetime);""")
        # Note that the above will still display a warning (not error) if the
        # table already exists
finally:
    connection.close()

# To Insert a single row into a table
try:
    with connection.cursor() as cursor:

        row = ("bob", 21, "1990-02-06 23:04:56")
        cursor.execute("INSERT INTO Friends VALUES (%s,%s,%s);", row)
        connection.commit()
finally:
    connection.close()

# To Insert multiple rows into a table
try:
    with connection.cursor() as cursor:

        rows = [("bob", 21, "1990-02-06 23:04:56"),
                ("jim", 56, "1955-05-09 13:12:45"),
                ("fred", 100, "1911-09-12 01:01:01")]
        cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", rows)
        connection.commit()
finally:
    connection.close()

# To update an entry
try:
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'Bob';")
        connection.commit()
finally:
    connection.close()

# An entry can also be updated using string interpretation
try:
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = %s WHERE name = %s", (23,'Bob'))
        connection.commit()
finally:
    connection.close()

# To update many rows
try:
    # A cursor is the object that is used to execute queries
    with connection.cursor() as cursor:
        rows = [(23, 'bob'), (24, 'jim'), (25, 'fred')]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;", rows)
        connection.commit()
finally:
    connection.close()

# To delete a row
try:
    # A cursor is the object that is used to execute queries
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM Friends WHERE name = 'Bob';")
        connection.commit()
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()

# To delete many rows (Delete where in)
try:
    with connection.cursor() as cursor:
        list_of_names = ['fred', 'Fred']
        # Prepare a string with same number of placeholders as in list_of_names
        format_strings = ','.join(['%s'] * len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names)
        connection.commit()
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()