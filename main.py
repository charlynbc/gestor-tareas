# Funcion para cargar el nombre del usuario
def cargar_usuario():
    
    try:
        with open("usuario.txt", "r", encoding="utf-8") as archivo:
            return archivo.read().strip()
    
    except FileNotFoundError:
        return None

# Funcion para guardar el nombre del usuario
def guardar_usuario(nombre):
    with open("usuario.txt", "w", encoding="utf-8") as archivo:
        archivo.write(nombre)
        

# Lista para almacenar las tareas
tareas = []

# Funcion para agregar una tarea
def agregar_tarea():
    tarea = input("Ingrese la tarea: ")
    tareas.append({"descripcion": tarea, "completada": False})
    print("Tarea agregada con éxito.")

# Funcion para mostrar las tareas
def lista_tareas():
    if not tareas:
        print("No hay tareas en la lista.")
    else:
        print("\nLista de tareas:")
        for i, tarea in enumerate(tareas, start=1):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{i}. {tarea['descripcion']} - {estado}")

# Funcion para marcar una tarea como completada
def completar_tarea():
    lista_tareas()
    if tareas:
        try:
            num= int(input("Ingrese el número de la tarea que desea marcar como completada: "))
            tareas[num-1]["completada"] = True
            print("Tarea marcada como completada.")
        except (ValueError, IndexError):
            print("Número de tarea inválido.")

# Funcion para guardar las tareas en un archivo
def guardar_tareas():
    with open("tareas.txt", "w", encoding="utf-8") as archivo:
        for tarea in tareas:
            archivo.write(f"{tarea['descripcion']},{tarea['completada']}\n")
    print("Tareas guardadas con éxito.")

#Funcion para cargar las tareas desde un archivo
def cargar_tareas():
    try:
        with open("tareas.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                descripcion, completada = linea.strip().split(",")
                tareas.append({"descripcion": descripcion, "completada": completada == "True"})
        print("Tareas cargadas con éxito.")
    except FileNotFoundError:
        print("No se encontró el archivo de tareas.")
        pass

#Funcion para eliminar una tarea
def eliminar_tarea():
    lista_tareas()
    if tareas:
        try:
            num = int(input("Ingrese el número de la tarea que desea eliminar: "))
            tareas.pop(num-1)
            print("Tarea eliminada con éxito.")
        except (ValueError, IndexError):
            print("Número de tarea inválido.")

# Menu Principal
def menu():
    nombre_usuario = cargar_usuario()
    if not nombre_usuario:
        nombre_usuario = input("Ingrese su nombre: ")
        guardar_usuario(nombre_usuario)

    cargar_tareas()

    while True:
        print(f"\nBienvenido, {nombre_usuario}!")
        print("1. Agregar tarea")
        print("2. Ver lista de tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Guardar tareas")
        print("6. Cambiar nombre de usuario")
        print("7. Cambiar de usuario")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            lista_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            guardar_tareas()
        elif opcion == "6":
            nuevo_nombre = input("Ingrese su nuevo nombre: ")
            guardar_usuario(nuevo_nombre)
            nombre_usuario = nuevo_nombre
        elif opcion == "7":
            nuevo_usuario = input("Ingrese el nombre del nuevo usuario: ")
            guardar_usuario(nuevo_usuario)
            nombre_usuario = nuevo_usuario
            tareas.clear()
            cargar_tareas()
        elif opcion == "8":
            guardar_tareas()
            print(f"¡Hasta luego {nombre_usuario}!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")






