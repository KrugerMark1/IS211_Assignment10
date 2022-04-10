CREATE TABLE artist (
	id INTEGER PRIMARY KEY,
	name TEXT
);

CREATE TABLE album (
	id INTEGER PRIMARY KEY,
	artist_id INTEGER,
    name TEXT
);

CREATE TABLE song (
	id INTEGER PRIMARY KEY,
    album_id INTEGER,
	name TEXT,
	track_number INTEGER,
	time_in_seconds INTEGER
);

INSERT INTO artist
(id, name)
VALUES
(1, "Bruno Mars");

INSERT INTO artist
(id, name)
VALUES
(2, "Eminem");

INSERT INTO artist
(id, name)
VALUES
(3, "Katy Perry");

INSERT INTO album
(id, artist_id, name)
VALUES
(1, 2, "Recovery");

INSERT INTO album
(id, artist_id, name)
VALUES
(2, 3, "Dark Horse");

INSERT INTO song
(id, album_id, name, track_number, time_in_seconds)
VALUES
(1, 1, "On Fire", 3, 214);

INSERT INTO song
(id, album_id, name, track_number, time_in_seconds)
VALUES
(2, 1, "Going Through Changes", 6, 359);

select * from artist
order by id desc;

select * from album
order by id desc;

select * from song
order by id desc;