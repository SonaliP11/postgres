from sqlalchemy import (
    create_engine, MetaData, Table, Column, Float, ForeignKey, Integer, String
)

# Excuting the instruction from our localhost "chinook" database
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create variable for the "Artist" table
artist_table = Table(
    "Artist", meta,
)

# making the connection
with db.connect() as connection:
    