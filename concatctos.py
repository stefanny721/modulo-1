contactos= {
    "maria":{
        "nombre_completo": "MARIA JOSE HERNANDEZ CARRILLO",
        "telefono": "31367872873",
        "direccion": "malambito efectivo "


    },
     "nicolas":{
         "nombre_completo": "NICOLAS DAVID TROCHA SIMANCAS",
         "telefono": "287283263",
          "direccion":"Rebolo "
     }
}

print(contactos.keys())
for key in enumerate (contactos):
print(i+1,"-", key)
print(contactos["maria"]["nombre_completo"])
