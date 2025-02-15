#importazione delle librerie
import random
import string
import pandas as pd

# Funzione per generare nomi casuali
def genera_nome():
    return ''.join(random.choices(string.ascii_uppercase, k=1)) + \
           ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 7)))

# Funzione per generare e-mail
def genera_email(nome, cognome):
    domini = ['gmail.com', 'yahoo.com', 'outlook.com']
    return f"{nome.lower()}.{cognome.lower()}@{random.choice(domini)}"

# Generazione dei dati
dati_utenti = []
for _ in range(10):
    nome = genera_nome()
    cognome = genera_nome()
    email = genera_email(nome, cognome)
    telefono = ''.join(random.choices(string.digits, k=10))
    dati_utenti.append({"Nome": nome, "Cognome": cognome, "Email": email, "Telefono": telefono})

# Creazione del file Excel
df = pd.DataFrame(dati_utenti)
df.to_excel("utenti.xlsx", index=False)
print("File Excel 'utenti.xlsx' creato con successo.")