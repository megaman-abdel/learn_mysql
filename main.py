import mysql.connector

from getpass import getpass
from mysql.connector import connect, Error

with connect(
    host="localhost",
    port=32006,
    user=input("Enter username: "),
    password=getpass("Enter password: "),
) as connection:
    print(connection)
    create_db_query = "SELECT * FROM dtm_live.test_LoadDataIntoWorkbench"
    with connection.cursor() as cursor:
        cursor.execute(create_db_query)
