import sqlite3

db_path = r'c:\Users\Juan\Downloads\EcoPulso_Completorr\EcoPulso_Completo\ecopulso2\ecopulso.db'
db = sqlite3.connect(db_path)

FACTOR = 217770 / 4470.0

# Update existing records
db.execute("UPDATE consumos SET kwh = ROUND(kwh * ?, 2), co2_kg = ROUND((kwh * ?) * 0.4 / 1000, 4) WHERE fecha NOT LIKE '2026-05%'", (FACTOR, FACTOR))

# Update the monthly goal so the dashboard efficiency makes sense
db.execute("UPDATE parametros SET valor = '220000' WHERE clave = 'meta_mensual_kwh'")

db.commit()
db.close()
print("Datos escalados y meta actualizada.")
