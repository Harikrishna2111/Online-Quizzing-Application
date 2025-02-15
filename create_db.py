import sqlite3
conn = sqlite3.connect('quiz_master_app.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    full_name TEXT NOT NULL,
    qualification TEXT,
    dob DATE
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Subject (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Chapter (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER,
    name TEXT NOT NULL,
    description TEXT,
    FOREIGN KEY (subject_id) REFERENCES Subject(id)
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Quiz (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chapter_id INTEGER,
    date_of_quiz DATETIME NOT NULL,
    time_duration TEXT,
    FOREIGN KEY (chapter_id) REFERENCES Chapter(id)
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Question (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quiz_id INTEGER,
    question_statement TEXT NOT NULL,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    option3 TEXT NOT NULL,
    option4 TEXT NOT NULL,
    correct_option INTEGER NOT NULL,
    FOREIGN KEY (quiz_id) REFERENCES Quiz(id)
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Score (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quiz_id INTEGER,
    user_id INTEGER,
    time_stamp_of_attempt DATETIME NOT NULL,
    total_score INTEGER NOT NULL,
    FOREIGN KEY (quiz_id) REFERENCES Quiz(id),
    FOREIGN KEY (user_id) REFERENCES User(id)
)
''')
conn.commit()
conn.close()

print("Database created successfully")
