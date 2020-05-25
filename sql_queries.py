# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("CREATE TABLE IF NOT EXISTS songplay(start_time timestamp, user_id int, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar)")

user_table_create = ("CREATE TABLE IF NOT EXISTS users(userId int PRIMARY KEY, firstName varchar, lastName varchar, gender varchar, level varchar)")

song_table_create = ("CREATE TABLE IF NOT EXISTS songs(song_id varchar PRIMARY KEY,title varchar, artist_id varchar, year int, duration float)")

artist_table_create = ("CREATE TABLE IF NOT EXISTS artists(artist_id varchar PRIMARY KEY, artist_name varchar, artist_location varchar, artist_latitude float, artist_longitude float)")

time_table_create = ("CREATE TABLE IF NOT EXISTS time(time_s timestamp PRIMARY KEY, hour int, day int, week int,month int, year int, weekday int)")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplay (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")
# user_columns = ['userId','firstName','lastName','gender','level']

user_table_insert = ("""INSERT INTO users(userId, firstName, lastName, gender, level)  VALUES (%s, %s, %s, %s, %s) ON CONFLICT (userId) DO NOTHING;
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, artist_name, artist_location, artist_latitude, artist_longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time (time_s, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (time_s) DO NOTHING;
""")

# FIND SONGS

song_select = ("""SELECT songs.song_id, artists.artist_id FROM songs JOIN artists ON songs.artist_id = artists.artist_id
    WHERE songs.title = %s
    AND artists.artist_name = %s
    AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]