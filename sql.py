import sqlite3 
con = sqlite3.connect("ask.db") # veri tabanına bağlantı, eğer veri tabanı yoksa dosya oluşturulacaktır.
cur = con.cursor()
from config import DATABASE

class DB_Manager:
    def create_table():
        conn = sqlite3.connect("ask.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS all_questions (
                username TEXT,
                question TEXT
            )
        ''')
        
        conn.commit()
        conn.close()


    def get_all_questions():
        conn = sqlite3.connect("ask.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM all_questions")
        questions = cursor.fetchall()
        conn.close()
        return questions


if __name__ == '__main__':
    manager = DB_Manager(DATABASE)