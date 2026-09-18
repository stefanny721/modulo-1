yo = {"nombre": "stefanny", "edad": 17, "es_estudiante": True}
yo_lista = ["stefanny", 18, False]
print(yo_lista[0])
print(yo["nombre"])

# para modificar una lista
yo_lista[0] = "Stefanny "
print(yo_lista)
yo["nombre"] = "Stefanny"
print(yo)

# Agregar un nuevo par

yo_lista.append("cra 45 #54-46")
yo["direccion"] = "cra 45 #54-46"
yo["telefono"] = "+57 3178976353"

#Update
yo_2 = {"rh": "o+", "profesion": "Cientifico de Datos"}
yo.update(yo_2)
print(yo)