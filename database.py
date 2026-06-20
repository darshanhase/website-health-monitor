import sqlite3

DB_NAME = "monitor.db"

# Initialize database with table
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            status TEXT,
            latency REAL,
            checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

# Insert new monitoring result
def insert_result(url, status, latency):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO results (url, status, latency) VALUES (?, ?, ?)", (url, str(status), latency))
    conn.commit()
    conn.close()

# Get all results for history page
def get_all_results():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT url, status, latency, checked_at FROM results ORDER BY checked_at DESC")
    rows = c.fetchall()
    conn.close()
    return rows
