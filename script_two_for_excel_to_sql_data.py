#importazione librerie
import sqlite3
import pandas as pd

#lettura del file Excel
df = pd.read_excel("utenti.xlsx")

#creazione del database SQLite
conn = sqlite3.connect('utenti.db')
cursor = conn.cursor()

#creazione della tabella
cursor.execute('''
        CREATE TABLE IF NOT EXISTS utenti (
            Nome TEXT,
            Cognome TEXT,
            Email TEXT,
            Telefono TEXT
        )
''')

#inserimento dati nella tabella
for _, row in df.iterrows():
    cursor.execute('''
        INSERT INTO utenti (Nome, Cognome, Email, Telefono)
        VALUES (?, ?, ?, ?)
''', (row['Nome'], row['Cognome'], row['Email'], row['Telefono']))
    
conn.commit()
conn.close()
print("Tabella SQL creata con successo.") 