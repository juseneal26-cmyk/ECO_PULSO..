import sqlite3
import os

db_path = r'c:\Users\Juan\Downloads\EcoPulso_Completorr\EcoPulso_Completo\ecopulso2\ecopulso.db'
db = sqlite3.connect(db_path)

db.execute("DELETE FROM consumos WHERE fecha LIKE '2026-05%'")

areas = ['Aulas','Laboratorios','Administrativo','Otros']
vals = [99883, 56025, 42875, 18987]

for i, area in enumerate(areas):
    co2 = round(vals[i] * 0.4 / 1000, 4)
    db.execute("INSERT INTO consumos(usuario_id,area,kwh,fecha,medidor,co2_kg) VALUES(?,?,?,?,?,?)", 
               (1, area, vals[i], '2026-05-10', f'MED-0{i+1}', co2))

db.commit()
db.close()
print("Datos de Mayo actualizados.")
