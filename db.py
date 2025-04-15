import sqlite3 as lite

con = lite.connect('jogo_da_velha.db')

with con:
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE veia (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vitoria_x INTEGER,
        vitoria_O INTEGER,
        empate INTEGER
    )
    ''')