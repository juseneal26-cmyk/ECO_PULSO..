import sqlite3
import os

db_path = r'c:\Users\Juan\Downloads\EcoPulso_Completorr\EcoPulso_Completo\ecopulso2\ecopulso.db'
db = sqlite3.connect(db_path)
count = db.execute("SELECT COUNT(*) FROM consumos WHERE fecha LIKE '2026-05%'").fetchone()[0]
if count == 0:
    areas = ['Aulas','Laboratorios','Administrativo','Otros']
    vals = [2050, 1150, 880, 390]
    for i, area in enumerate(areas):
        co2 = round(vals[i]*0.4/1000, 4)
        db.execute("INSERT INTO consumos(usuario_id,area,kwh,fecha,medidor,co2_kg) VALUES(?,?,?,?,?,?)", (1, area, vals[i], '2026-05-10', f'MED-0{i+1}', co2))
    db.commit()
    print("Consumos añadidos para Mayo 2026.")
else:
    print("Ya existen consumos para Mayo 2026.")
db.close()
