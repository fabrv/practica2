create table d_albums (
    id serial primary key,
    uri varchar(255) not null,
    name varchar(255) not null
  )

  create table d_artists (
    id serial primary key,
    uri varchar(255) not null,
    name varchar(255) not null
  )

  create table d_tracks (
    id serial primary key,
    uri varchar(255) not null,
    name varchar(255) not null,
    artist_name varchar(255) not null,
    duration int not null,
    album_name varchar(255) not null
  )

  create table d_playlists (
    id serial primary key,
    bk_id varchar(255) not null,
    name varchar(255) not null,
    collaborative boolean not null,
    last_modified_at timestamp not null,
    num_followers int not null,
    num_edits int not null
  )

  CREATE TABLE f_playlist_tracks(
    id bigint primary key,
    sk_playlist bigint,
    sk_artist bigint,
    sk_album bigint,
    sk_track bigint,
    track_position int,
     CONSTRAINT fk_playlist
      FOREIGN KEY(sk_playlist)
	  REFERENCES d_playlists(id)
	  ON DELETE CASCADE,
	  CONSTRAINT fk_artist
      FOREIGN KEY(sk_artist)
	  REFERENCES d_artists(id)
	  ON DELETE CASCADE,
	  CONSTRAINT fk_album
      FOREIGN KEY(sk_album)
	  REFERENCES d_albums(id)
	  ON DELETE CASCADE,
	  CONSTRAINT fk_track
      FOREIGN KEY(sk_track)
	  REFERENCES d_tracks(id)
	  ON DELETE CASCADE
);