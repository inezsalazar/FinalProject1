import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    image TEXT
)
""")

cursor.execute("""
INSERT INTO products (name, price, image)
VALUES
("Resin Pendant", 25.00, "images/pendant1.jpg"),
("Resin Coaster Set", 40.00, "images/coaster1.jpg"),
("Resin Tray", 55.00, "images/tray1.jpg")
""")

conn.commit()
conn.close()

print("Database created!")
