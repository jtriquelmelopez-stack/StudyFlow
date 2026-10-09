def pedir_tiempo_total():
    while True:
        try:
            tiempo_total = int(input("Ingrese el tiempo total disponible para estudiar en minutos: "))
            if tiempo_total > 0:
                return tiempo_total
            print("El tiempo debe ser mayor que 0.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def pedir_tareas():
    tareas = []
    while True:
        while True:
            nombre = input("Ingrese el nombre de la tarea (o 'salir' para terminar): ").strip()
            if nombre.lower() == "salir":
                return tareas
            if nombre:  # Valida que el nombre no esté vacío
                break
            print("El nombre de la tarea es obligatorio. Por favor, ingrese un nombre válido.")

        while True:
            try:
                prioridad = int(input("Ingrese la prioridad de la tarea (1 = Baja, 2 = Media, 3 = Alta): "))
                if prioridad in (1, 2, 3):
                    break
                print("La prioridad debe ser 1, 2 o 3.")
            except ValueError:
                print("Ingrese un valor numérico válido.")

        tareas.append({"nombre": nombre, "prioridad": prioridad})

def peso_prioridad(prioridad):
    if prioridad == 1:
        return 1
    elif prioridad == 2:
        return 2
    elif prioridad == 3:
        return 3
    else:
        return 0

def calcular_distribucion(tiempo_total, tareas):
    total_peso = sum(peso_prioridad(tarea["prioridad"]) for tarea in tareas)

    if total_peso == 0:
        print("No se pudo calcular la distribución porque no hay prioridades válidas.")
        return []

    distribucion = []
    for tarea in tareas:
        peso = peso_prioridad(tarea["prioridad"])
        tiempo = (peso / total_peso) * tiempo_total
        distribucion.append({
            "nombre": tarea["nombre"],
            "prioridad": tarea["prioridad"],
            "peso": peso,
            "tiempo": tiempo
        })

    return distribucion

def mostrar_resultado(distribucion):
    print("\nDistribución final del tiempo de estudio:")
    print("-" * 40)
    for item in distribucion:
        print(f"{item['nombre']} | Prioridad: {item['prioridad']} | Peso: {item['peso']} | Tiempo: {item['tiempo']:.2f} minutos")
    print("-" * 40)

def main():
    tiempo_total = pedir_tiempo_total()
    tareas = pedir_tareas()

    if not tareas:
        print("No se registraron tareas. No hay distribución que mostrar.")
        return

    distribucion = calcular_distribucion(tiempo_total, tareas)
    mostrar_resultado(distribucion)

if __name__ == "__main__":
    main()
