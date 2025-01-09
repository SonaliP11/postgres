import psycopg2

# Connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# Build a cursor object of database
cursor = connection.cursor()

# Query 1
# cursor.execute('SELECT * FROM "Artist"')

# Query 2
cursor.execute('SELECT "Name" FROM "Artist"')

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# results = cursor.fetchone()

# Close the connection
connection.close()

# Print the results
for result in results:
    print(result)
