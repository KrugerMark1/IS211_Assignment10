import sqlite3

"""
	What is the purpose of the person_pet table? This table groups a relationship together
	to help associate each table with one another. 
"""


def create_connection(db_file):
    """ create a database connection to the SQLite database
		specified by db_file
	:param db_file: database file
	:return: Connection object or None
	"""
    conn = sqlite3.connect(db_file)
    return conn


def select_person(conn, id_number):
    cur = conn.cursor()
    cur.execute('SELECT * FROM person WHERE id=?', (id_number,))

    rows = cur.fetchall()
    user_exists = True if len(rows) > 0 else False

    if user_exists:
        for row in rows:
            print(row)
    else:
        print("Error: Person not found.")


def main():
    conn = create_connection("pets.db")

    id_number = int(input("Please enter a Person ID number: "))

    while id_number != -1:
        select_person(conn, id_number)

        id_number = int(input("Please enter a Person ID number: "))

    print("Exiting...")

    # Close the connection
    conn.close()


if __name__ == '__main__':
    main()
