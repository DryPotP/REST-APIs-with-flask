import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
#id must be auto incrementing id then we have to use INTEGER PRIMARY KEY
cursor.execute(create_table)


create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(create_table)


connection.commit()

connection.close()
