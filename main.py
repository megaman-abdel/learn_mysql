def construct_import_query(shard):
    with open("generic_import.sql", "r") as file:
        query = file.read().replace("<IN_FILE>", shard)
    return query


import os, glob
import mysql.connector

from getpass import getpass
from mysql.connector import connect, Error

TARGET_DIR = "/Users/abdelmegahed/Desktop/sidel-work"

with connect(
    host="localhost",
    port=32006,
    user=input("Enter username: "),
    password=getpass("Enter password: "),
) as connection:
    with connection.cursor() as cursor:

        directories = list(filter(os.path.isdir, os.listdir(TARGET_DIR)))

        for d in directories:
            for shard in glob.glob(f"{TARGET_DIR}/{d}/*.csv"):
                query = construct_import_query(shard)
                cursor.execute(query)
        
