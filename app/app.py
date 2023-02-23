# import libraries
import json
# impost posgtresql
import psycopg2

# read json file
with open('mpd.slice.1000-1999.json') as data_file:
  data = json.load(data_file)

albums = []
artists = []
tracks = []
playlists = []
playlist_tracks = []

# get all the data from the json file
for playlist in data['playlists']:
  playlists.append((playlist['pid'], playlist['name'], playlist['collaborative'], playlist['modified_at'], playlist['num_followers'], playlist['num_edits']))
  for track in playlist['tracks']:
    tracks.append((track['track_uri'], track['track_name'], track['artist_name'], track['duration_ms'], track['album_name']))
    albums.append((track['album_uri'], track['album_name']))
    artists.append((track['artist_uri'], track['artist_name']))
    '''
          sk_playlist bigint,
          sk_artist bigint,
          sk_album bigint,
          sk_track bigint,
          track_position int,
    '''
    playlist_tracks.append((len(playlist) - 1, len(artists) - 1, len(albums) - 1, len(tracks) - 1, track['pos']))

# remove duplicates
albums = list(set(albums))
artists = list(set(artists))
tracks = list(set(tracks))

# connect to the database
conn = psycopg2.connect("dbname=spotify user=postgres password=postgres")
cur = conn.cursor()

# insert into database
for album in albums:
  cur.execute("INSERT INTO albums (uri, name) VALUES (%s, %s)", album)

for artist in artists:
  cur.execute("INSERT INTO artists (uri, name) VALUES (%s, %s)", artist)

for track in tracks:
  cur.execute("INSERT INTO tracks (uri, name, artist_name, duration, album_name) VALUES (%s, %s, %s, %s, %s)", track)

for playlist in playlists:
  cur.execute("INSERT INTO playlists (bk_id, name, collaborative, last_modified_at, num_followers, num_edits) VALUES (%s, %s, %s, %s, %s, %s)", playlist)

# insert playlist tracks
for playlist_track in playlist_tracks:
  cur.execute("INSERT INTO playlist_tracks (sk_playlist, sk_artist, sk_album, sk_track, track_position) VALUES (%s, %s, %s, %s, %s)", playlist_track)

