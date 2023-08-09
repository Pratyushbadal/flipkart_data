import sqlite3


class DbModel:
    def __init__(self):
        self.conn = sqlite3.connect("flipkart_data.db")
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT,
                price TEXT,
                description TEXT,
                reviews TEXT,
                image_url TEXT
            )
        """)
        self.conn.commit()

    def insert_data(self, data):
        self.cursor.execute("""
            INSERT INTO products (product_name, price, description, reviews, image_url)
            VALUES (?, ?, ?, ?, ?)
        """, data)
        self.conn.commit()

    def close_db_connection(self):
        self.conn.close()


if __name__ == "__main__":
    db = DbModel()
    db.create_table()
    db.close_db_connection()
