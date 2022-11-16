import sqlite3

conn = sqlite3.connect('nutrition_database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE nutrition ( username TEXT, email TEXT, password TEXT )')
print("Table created successfully")
conn.close()
