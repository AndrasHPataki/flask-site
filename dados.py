import sqlite3

with sqlite3.connect("banco.db") as connection:
    c = connection.cursor()
    #c.execute("CREATE TABLE postagens(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,titulo TEXT, autor TEXT, post TEXT)")
    c.execute('INSERT INTO postagens VALUES("1","Criar site em flask", "András Pataki", "Tutorial de como construir seu site completo em flask...")')
    c.close()
