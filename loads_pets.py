import sqlite3

"""
	What is the purpose of the person_pet table? This table groups a relationship together
	to help associate each table with one another. 
"""

def create_database(conn):
	create_table_person = '''CREATE TABLE person(
		id INTEGER PRIMARY KEY,
		first_name TEXT,
		last_name TEXT,
		age INTEGER
	);'''

	create_table_pet = '''CREATE TABLE pet(
		id INTEGER PRIMARY KEY,
		name TEXT,
		breed TEXT,
		age INTEGER,
		dead INTEGER
	);'''

	create_table_person_pet = '''CREATE TABLE person_pet(
		person_id INTEGER,
		pet_id INTEGER
	);'''

	cur = conn.cursor()

	cur.execute(create_table_person)
	cur.execute(create_table_pet)
	cur.execute(create_table_person_pet)

	conn.commit()

def create_connection(db_file):
	conn = sqlite3.connect(db_file)
	return conn

def create_person(conn, data):
	sql = '''INSERT INTO person
			(id, first_name, last_name, age)
            VALUES
            (?, ?, ?, ?)'''

	cur = conn.cursor()
	cur.execute(sql, data)
	conn.commit()

def create_pet(conn, data):
	sql = '''INSERT INTO pet
			(id, name, breed, age, dead)
            VALUES
            (?, ?, ?, ?, ?)'''

	cur = conn.cursor()
	cur.execute(sql, data)
	conn.commit()

def create_person_pet(conn, data):
	sql = '''INSERT INTO person_pet
			(person_id, pet_id)
            VALUES
            (?, ?)'''

	cur = conn.cursor()
	cur.execute(sql, data)
	conn.commit()

def main():
	conn = create_connection("pets.db")

	create_database(conn)

	# Person
	Persons = [
		(1, 'James', 'Smith', 41),
		(2, 'Diana', 'Greene', 23),
		(3, 'Sara', 'White', 27),
		(4, 'William', 'Gibson', 23)
	]

	# Pets
	Pets = [
		(1, 'Rusty', 'Dalmation', 4, 1),
		(2, 'Bella', 'Alaskan Malamute', 3, 0),
		(3, 'Max', 'Cocker Spaniel', 1, 0),
		(4, 'Rocky', 'Beagle', 7, 0),
		(5, 'Rufus', 'Cocker Spaniel', 1, 0),
		(6, 'Spot', 'Bloodhound', 2, 1)
	]

	# Person Pets
	Person_Pets = [
		(1, 1),
		(1, 2),
		(2, 3),
		(2, 4),
		(3, 5),
		(4, 6)
	]

	for person in Persons:
		create_person(conn, person)

	for pet in Pets:
		create_pet(conn, pet)

	for person_pet in Person_Pets:
		create_person_pet(conn, person_pet)

	# Close the connection
	conn.close()

if __name__ == '__main__':
	main()
