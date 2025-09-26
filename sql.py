

import sqlite3 

class DB_Manager:
    def __init__(self, db_name):
        self.db_name = db_name 
        self.create_table() 
        
    def create_table(self):
        conn = sqlite3.connect(self.db_name) 
        cursor = conn.cursor()
        
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS all_questions (
                kullanici_id INTEGER,
                username TEXT,
                question TEXT
            )
        ''')
        
        conn.commit()
        conn.close()

    def add_question(self, user_id, username, question_text):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO all_questions (kullanici_id, username, question) VALUES (?, ?, ?)",(user_id, username, question_text))
        conn.commit()
        conn.close()
        
    def get_all_questions(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM all_questions")
        questions = cursor.fetchall()
        
        conn.close()
        return questions

if __name__ == '__main__':
    DATABASE_NAME = "ask.db"
    manager = DB_Manager(DATABASE_NAME)
    
