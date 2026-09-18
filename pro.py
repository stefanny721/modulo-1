nombres = []
telefonos = []
emails = []
direcciones = []

contactos = {}

while True:
    menu = """
    ### ELIGUE UNA OPCION

    1. Agregar un contacto
    2. Buscar un contacto
    3. Eliminar un contacto
    4. Ver Contacto
    5.Salir
    """
    opcion_elegida = int(input(menu))

    if opcion_elegida == 1:
        nombre = input("Ingrese el nombre")
        telefono = input("Ingrese el telefono")
        email = input("Ingrese el email")
        direccion = "Ingrese la direccion"
        contactos[nombre] = {
            "Email": email,
            "telefono": telefono,
            "direccion": direccion,
        }

        nombres.append(nombre)
        telefonos.append(telefono)
        emails.append(email)
        direcciones.append(direccion)
        print(f"Contacto {nombre} guardado exitosamente")
    elif opcion_elegida == 2:
        nombre = input("Ingrese el nombre a buscar: ")
        if nombre in nombres:
            indice = nombres.index(nombre)
            print("=" * 10)
            print(f"Nombre: {nombre}")
            print(f"Telefono: {telefono}")
            print(f"Email: {email}")
            print(f"Direccion: {direccion}")
            print("====================")

            print("Si se encuentra")
        else:
            print("Contacto no encontrado")

    elif opcion_elegida == 3:
        nombre = input("Ingrese el nombre del contacto a eliminar:")
        if nombre in nombres:
            indice = nombres.index(nombre.lower())
            nombres.pop(indice)
            telefonos.pop(indice)
            emails.pop(indice)
            direcciones.pop(indice)
            print(f"Contacto {nombre} eliminado exitosamente")
    elif opcion_elegida == 4:
        print(contactos.keys())
        for key in enumerate(contactos):
            print(i + 1, "-", key)

    elif opcion_elegida == 5:
        print("Hasta la vista baby")
        break
    else:
        print("opcion invalida intenta nuevamente")
