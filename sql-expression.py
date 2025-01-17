from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# Excuting the instruction from our localhost "chinook" database
db = create_engine("postgresql:///chinook")

meta = MetaData()


# create variable for the "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for the "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create variable for the "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)


# making the connection
with db.connect() as connection:

    # Query 1 Select all records from the "Artist" table
    # select_query = artist_table.select()

    # Query 2 Select only the "Name" column from the artist table
    # select_query = artist_table.select().with_only_columns(artist_table.c.Name)

    # Query 3 Select only queen from the artist table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query 4 Select only by "ArtistId" #51 from the artist table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 Select only the albums with 'artistId' #51 on the "Album" table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 Select all tracks where the composer is "Queen" from the "Track" table
    select_query = track_table.select().where(track_table.c.Composer == "Queen")


    results = connection.execute(select_query)
    for result in results:
        print(result)
        