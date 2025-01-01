import sqlite3


def add_wager(game_id, wager, balance):
    conn = sqlite3.connect('Main.db')

    try:
        cursor = conn.cursor()
        # Correct the syntax for the INSERT query
        cursor.execute("INSERT INTO Game_Wagers (game_id, wager, balance) VALUES (?, ?, ?)", (game_id, wager, balance))
        conn.commit()
    finally:
        conn.close()


def create_db():
    conn = sqlite3.connect('Main.db')
    try:
        cursor = conn.cursor()

        # Create the table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Game_Wagers (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            game_id INTEGER, 
            wager INTEGER, 
            balance INTEGER, 
            FOREIGN KEY(game_id) REFERENCES Games(id)
        )
        """)

        # Insert data into the table
        cursor.execute("""
        INSERT INTO Game_Wagers (game_id, wager, balance) VALUES (?, ?, ?)
        """, (1, 100, 500))
        conn.commit()

        # Fetch and print all rows from the table
        cursor.execute("SELECT * FROM Game_Wagers")
        print(cursor.fetchall())
    finally:
        conn.close()


def create_game_id():
    conn = sqlite3.connect('Main.db')
    try:
        cursor = conn.cursor()

        # Create the table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS game_id (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            game_id INTEGER
        )
        """)
        conn.commit()

        # Get the current maximum game_id
        cursor.execute("SELECT MAX(game_id) FROM game_id")
        max_game_id = cursor.fetchone()[0]

        # Increment the game_id by 1
        new_game_id = (max_game_id + 1) if max_game_id else 1

        # Insert the new game_id into the table
        cursor.execute("INSERT INTO game_id (game_id) VALUES (?)", (new_game_id,))
        conn.commit()

        return new_game_id

    finally:
        conn.close()

def get_balance(game_id):
        conn = sqlite3.connect('Main.db')
        try:
            cursor = conn.cursor()

            # Fetch the balance from the Game_Wagers table for the given game_id
            cursor.execute("SELECT balance FROM Game_Wagers WHERE game_id=?", (game_id,))
            balance = cursor.fetchone()[0]
            return balance

        finally:
            conn.close()


# Example usage
if __name__ == "__main__":
    print("New Game ID:", create_game_id())
    create_db()
