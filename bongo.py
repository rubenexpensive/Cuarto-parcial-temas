from pymongo import MongoClient

client = MongoClient('localhost', 27017,) 

db = client.prueba # Crea bd , primera forma
# db.name
tabla= db.unacoleccion
print(tabla)

import json

with open("sample.json") as arch:
    a = json.load(arch)
    
tabla.insert_many(a)

db2 = client['bd-prueba'] # Crea base de datos, 2da forma, noten que como la sintaxis de un diccionario de pyhton
collec = db2.estudiantes

estudiante = {
    "_id" : 20,
    "nombre" : "Pedro Fernández",
    "universidad" : "UIS",
    "carrera" : "Economía",
    "semestre" : "2021-2"
}
db2['bd-prueba'].insert_one(estudiante) # Crea una colección e inserta un documento 