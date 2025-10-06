import sqlite3

kobling = sqlite3.connect("bokbutikk.db")

c = kobling.cursor()

c.execute("""
 CREATE TABLE IF NOT EXISTS inventar(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     tittel TEXT NOT NULL,
     pris REAL,
     antall INTEGER NOT NULL
 )     
""")
def legg_til_vare():
    tittel = input("Tittel:")
    pris = input("Pris:")
    antall = input("Antall:")
    c.execute("INSERT INTO inventar (tittel,pris,antall) VALUES (?,?,?)",(tittel,pris,antall))
    kobling.commit()

def slett_vare():
    c.execute("SELECT id,tittel FROM inventar")
    rader = c.fetchall()
    for rad in rader:
        print(rad)
    slettes = input("Skriv inn id til bok som skal slettes:")
    c.execute("DELETE FROM inventar WHERE id =?",(slettes))
    c.execute("SELECT tittel FROM inventar WHERE id = ?",
    (slettes))
    boktittel = c.fetchone()
    print (f"{boktittel[0]} slettes ")
    kobling.commit()
inn = ""
while inn != "q":
    print("""
MENY
1. Legg til vare
2. Slett vare
q Avslutt  
""")
    inn = input(":")
    if inn == "1":
        legg_til_vare()
    elif inn == "2":
        slett_vare()








# c.execute("INSERT INTO inventar (tittel,pris,antall) VALUES (?,?,?)" ,("Ringenes Herre", 299.90,70))

# kobling.commit()

# c.execute("SELECT * FROM inventar")
# rader = c.fetchall()
# for rad in rader:
#      print(rad)