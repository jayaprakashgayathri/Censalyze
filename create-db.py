import sqlite3

conn = sqlite3.connect('census.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS population_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        mortality_rate REAL,
        birthrate REAL,
        income_per_head REAL,
        sex_ratio REAL,
        entry_date TEXT
    )
''')

conn.commit()
conn.close()
print("Database and table 'population_data' created successfully!")
