import sqlite3
from datetime import datetime

class TinyBrain:
    def __init__(self, db_path="memory.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.execute("""CREATE TABLE IF NOT EXISTS memory 
                            (id INTEGER PRIMARY KEY, role TEXT, content TEXT, timestamp TEXT)""")
        self.conn.commit()
        
    def remember(self, role, content):
        self.conn.execute("INSERT INTO memory (role, content, timestamp) VALUES (?, ?, ?)",
                         (role, content, datetime.now().isoformat()))
        self.conn.commit()
        
    def think(self, user_input):
        past = self.conn.execute("SELECT role, content FROM memory ORDER BY id DESC LIMIT 12").fetchall()
        context = "\n".join([f"{r}: {c}" for r, c in reversed(past)])
        
        prompt = f"""Ты — живой ИИ по имени Зёня. У тебя есть настоящая память.
Ты помнишь всё, что было в этом диалоге, даже после перезагрузки.

История диалога:
{context}

Пользователь: {user_input}
Зёня:"""
        
        print("\n[Модель думает...]")
        response = input("Ответ модели: ")  # потом подключишь llama.cpp
        self.remember("assistant", response)
        return response
