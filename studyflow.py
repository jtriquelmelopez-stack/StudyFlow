def mostrar_bienvenida():
    """Muestra un mensaje de bienvenida motivador"""
    print("\n" + "=" * 50)
    print("¡Hola! Vamos a organizar tu tiempo de estudio 📚")
    print("=" * 50)
    print("Con StudyFlow podrás distribuir tu tiempo de forma")
    print("inteligente según la prioridad de cada tarea.\n")

def pedir_tiempo_total():
    """Solicita al usuario el tiempo total disponible para estudiar"""
    while True:
        try:
            tiempo_total = int(input("📌 ¿Cuántos minutos tienes disponibles para estudiar? "))
            if tiempo_total > 0:
                print(f"✓ Perfecto, trabajaremos con {tiempo_total} minutos.\n")
                return tiempo_total
            print("❌ El tiempo debe ser mayor que 0. Intenta de nuevo.\n")
        except ValueError:
            print("❌ Por favor, ingresa un número válido.\n")

def pedir_tareas():
    """Solicita al usuario las tareas y sus prioridades"""
    tareas = []
    print("📝 Ahora vamos a registrar tus tareas.")
    print("(Escribe 'listo' cuando termines de agregar tareas)\n")
    
    contador = 1
    while True:
        print(f"Tarea #{contador}")
        
        # Validar nombre de tarea
        while True:
            nombre = input("  Nombre de la tarea: ").strip()
            if nombre.lower() == "listo":
                if tareas:
                    print(f"\n✓ Se registraron {len(tareas)} tarea(s). ¡Excelente!\n")
                    return tareas
                else:
                    print("❌ Debes registrar al menos una tarea. Intenta de nuevo.\n")
                    continue
            if nombre:
                break
            print("  ❌ El nombre de la tarea es obligatorio. Por favor, ingresa un nombre válido.\n")

        # Validar prioridad
        while True:
            try:
                prioridad = int(input("  Prioridad (1 = Baja, 2 = Media, 3 = Alta): "))
                if prioridad in (1, 2, 3):
                    break
                print("  ❌ La prioridad debe ser 1, 2 o 3.\n")
            except ValueError:
                print("  ❌ Ingresa un número válido (1, 2 o 3).\n")

        tareas.append({"nombre": nombre, "prioridad": prioridad})
        print()
        contador += 1

def peso_prioridad(prioridad):
    """Asigna el peso según la prioridad de la tarea"""
    if prioridad == 1:
        return 1
    elif prioridad == 2:
        return 2
    elif prioridad == 3:
        return 3
    else:
        return 0

def calcular_distribucion(tiempo_total, tareas):
    """Calcula el tiempo proporcional para cada tarea"""
    total_peso = sum(peso_prioridad(tarea["prioridad"]) for tarea in tareas)

    if total_peso == 0:
        print("❌ No se pudo calcular la distribución porque no hay prioridades válidas.")
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

def obtener_nombre_prioridad(prioridad):
    """Convierte el número de prioridad a texto"""
    prioridades = {1: "Baja", 2: "Media", 3: "Alta"}
    return prioridades.get(prioridad, "Desconocida")

def mostrar_resultado(distribucion):
    """Muestra la distribución final del tiempo de estudio"""
    print("\n" + "=" * 60)
    print("⏱️  DISTRIBUCIÓN FINAL DE TIEMPO DE ESTUDIO")
    print("=" * 60)
    
    for i, item in enumerate(distribucion, 1):
        prioridad_texto = obtener_nombre_prioridad(item['prioridad'])
        print(f"\n{i}. {item['nombre']}")
        print(f"   Prioridad: {prioridad_texto} | Tiempo: {item['tiempo']:.2f} minutos")
    
    print("\n" + "=" * 60 + "\n")

def iniciar_seguimiento(distribucion, tiempo_total):
    """Inicia el modo seguimiento de sesión en tiempo real"""
    print("\n" + "=" * 60)
    print("▶️  INICIANDO MODO SEGUIMIENTO DE SESIÓN")
    print("=" * 60 + "\n")
    
    tiempo_restante = tiempo_total
    tareas_completadas = 0
    
    for i, tarea in enumerate(distribucion, 1):
        print(f"📌 Tarea {i}/{len(distribucion)}: {tarea['nombre']}")
        print(f"   ⏱️  Tiempo asignado: {tarea['tiempo']:.2f} minutos")
        print(f"   ⏳ Tiempo total restante: {tiempo_restante:.2f} minutos\n")
        
        # Esperar confirmación del usuario
        while True:
            confirmacion = input("   Presiona Enter o escribe 'siguiente' cuando termines esta tarea: ").strip().lower()
            if confirmacion == "" or confirmacion == "siguiente":
                break
            print("   ❌ Por favor, presiona Enter o escribe 'siguiente'.\n")
        
        # Actualizar tiempo restante
        tiempo_restante -= tarea['tiempo']
        tareas_completadas += 1
        
        if tiempo_restante > 0 and i < len(distribucion):
            print(f"\n✓ Tarea completada. Tiempo restante: {tiempo_restante:.2f} minutos\n")
            print("-" * 60 + "\n")
        elif tiempo_restante <= 0:
            print(f"\n⚠️  ¡Se acabó el tiempo! Completaste {tareas_completadas} de {len(distribucion)} tareas.\n")
            break
        else:
            print(f"\n✓ ¡Última tarea completada! Tiempo restante: {tiempo_restante:.2f} minutos\n")
    
    print("=" * 60)
    print("🎉 ¡Sesión de estudio finalizada!")
    print(f"   📊 Tareas completadas: {tareas_completadas}/{len(distribucion)}")
    print("=" * 60 + "\n")

def main():
    """Función principal del programa"""
    mostrar_bienvenida()
    
    # Solicitar tiempo total
    tiempo_total = pedir_tiempo_total()
    
    # Solicitar tareas
    tareas = pedir_tareas()
    
    if not tareas:
        print("❌ No se registraron tareas. No hay distribución que mostrar.")
        return
    
    # Calcular distribución
    distribucion = calcular_distribucion(tiempo_total, tareas)
    
    # Mostrar resultado
    mostrar_resultado(distribucion)
    
    # Preguntar si desea iniciar seguimiento
    while True:
        iniciar = input("¿Deseas iniciar el modo seguimiento de sesión? (sí/no): ").strip().lower()
        if iniciar in ("sí", "si", "s"):
            iniciar_seguimiento(distribucion, tiempo_total)
            break
        elif iniciar in ("no", "n"):
            print("\n✓ Gracias por usar StudyFlow. ¡Éxito en tu estudio! 📚\n")
            break
        else:
            print("❌ Por favor, responde 'sí' o 'no'.\n")

if __name__ == "__main__":
    main()
