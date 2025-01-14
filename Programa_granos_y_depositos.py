# CREACION DE MATRIZ
def crear_matriz(valor_inicial: any, filas: int, columnas: int) -> list:
    """
    Crea una matriz de dimensiones dadas con un valor inicial para todas sus celdas.

    :param valor_inicial: El valor inicial de cada celda de la matriz.
    :param filas: Número de filas de la matriz.
    :param columnas: Número de columnas de la matriz.
    :return: La matriz creada.
    """
    matriz_cereales = []
    for i in range(filas):
        fila = [valor_inicial] * columnas
        matriz_cereales += [fila]

    return matriz_cereales


def granos_a_utilizar():
    """
    Retorna la lista de los nombres de los cereales disponibles.

    :return: Lista de nombres de cereales.
    """
    return ["Maiz", "Trigo", "Cebada", "Centeno"]


def cargar_primera_linea(matriz_cereales: list, granos):
    """
    Carga los nombres de los cereales en la primera fila de la matriz.

    :param matriz_cereales: La matriz donde se cargarán los cereales.
    :param granos: Lista de nombres de los cereales.
    :return: La matriz actualizada con los nombres de los cereales en la primera fila.
    """
    for j in range(len(granos)):
        matriz_cereales[0][j] = granos[j]
    return matriz_cereales


def cargar_matriz(matriz_cereales: list):
    """
    Carga las existencias de cada cereal en todos los depósitos.

    :param matriz_cereales: La matriz donde se almacenarán las existencias.
    :return: La matriz con las existencias cargadas.
    """
    print("Cargar la existencia de cada grano en todos los depositos.")
    for i in range(1, len(matriz_cereales)):
        for j in range(4):
            linea = int(input(f"Ingrese el deposito {i} del cereal {matriz_cereales[0][j]} en kg: "))
            while linea > 20000 or linea < 5000:
                linea = int(input(f"Error. La cantidad debe estar entre 5000 y 20000. Ingrese nuevamente: "))
            matriz_cereales[i][j] = linea
    return matriz_cereales


def mostrar_matriz(matriz_cereales):
    """
    Muestra la matriz de existencias de cereales.

    :param matriz_cereales: La matriz con las existencias cargadas.
    """
    print("Tabla resultante:")
    for i in matriz_cereales:
        print("|", end=" ")
        for j in i:
            print(f"{j:<10}|", end=" ")
        print()


def calcular_sumatoria_fila(matriz_cargada):
    """
    Calcula la sumatoria de kilos almacenados en cada depósito.

    :param matriz_cargada: La matriz con las existencias cargadas.
    :return: Lista con la sumatoria de kilos por depósito.
    """
    sumatoria_fila = []
    for i in range(1, len(matriz_cargada)):
        sumatoria = 0
        for j in range(len(matriz_cargada[i])):
            sumatoria += int(matriz_cargada[i][j])
        sumatoria_fila.append(sumatoria)
    return sumatoria_fila


def mostrar_sumatoria_fila(sumatoria_fila):
    """
    Muestra la cantidad total de kilos almacenados en cada depósito.

    :param sumatoria_fila: Lista con la sumatoria de kilos por depósito.
    """
    print("La cantidad total de kilos almacenados en cada deposito:")
    for i in range(len(sumatoria_fila)):
        print(f"Deposito {i + 1}: {sumatoria_fila[i]}")


def calcular_minimos(matriz_cargada, granos):
    """
    Calcula el cereal que almacenó menos kilos en cada depósito.

    :param matriz_cargada: La matriz con las existencias cargadas.
    :param granos: Lista de nombres de los cereales.
    :return: Lista con los cereales que almacenaron menos kilos en cada depósito.
    """
    minimo = float('inf')
    nombre_minimo = []

    for j in range(len(matriz_cargada[0])):
        for i in range(1, len(matriz_cargada)):
            numero = int(matriz_cargada[i][j])
            if numero < minimo:
                minimo = numero
                nombre_minimo = [granos[j]]
            elif numero == minimo:
                nombre_minimo.append(granos[j])

    return nombre_minimo


def eliminar_duplicados_y_formatear(lista):
    """
    Elimina duplicados de una lista mientras conserva el orden y devuelve un string formateado.

    :param lista: Lista con elementos duplicados.
    :return: String con los elementos únicos, separados por coma.
    """
    lista_unica = []
    for elemento in lista:
        if elemento not in lista_unica:
            lista_unica.append(elemento)
    return ", ".join(lista_unica)


def maxima_cantidad_kg(matriz_cargada, granos):
    """
    Calcula la máxima cantidad de kilos almacenados de cada cereal.

    :param matriz_cargada: La matriz con las existencias cargadas.
    :param granos: Lista de nombres de los cereales.
    """
    maximos_kg = []
    for j in range(len(matriz_cargada[0])):
        numero_maximo = 0
        granos_maximo = ""
        for i in range(1, len(matriz_cargada)):
            numero = int(matriz_cargada[i][j])
            if numero > numero_maximo:
                numero_maximo = numero
                granos_maximo = granos[j]
        maximos_kg.append((granos_maximo, numero_maximo))

    print("Depósito con mayor kilogramos por cereal:")
    for i in range(len(maximos_kg)):
        print(f"{maximos_kg[i][0]}: {maximos_kg[i][1]} kg")


def precios_cereales():
    """
    Retorna los precios por kilo de cada cereal.

    :return: Lista con los precios de los cereales.
    """
    return [512, 250, 600, 700]


def calcular_total_cereales(matriz_cargada):
    """
    Calcula la sumatoria total de kilos almacenados por cada cereal.

    :param matriz_cargada: La matriz con las existencias cargadas.
    :return: Lista con la sumatoria de kilos por cereal.
    """
    sumatoria_columna = []
    for j in range(len(matriz_cargada[0])):
        suma = 0
        for i in range(1, len(matriz_cargada)):
            suma += int(matriz_cargada[i][j])
        sumatoria_columna.append(suma)
    return sumatoria_columna


def recaudar_cereales(sumatoria_columna, precio_cereal):
    """
    Calcula la recaudación total por cereal multiplicando las cantidades por los precios.

    :param sumatoria_columna: Lista con la sumatoria de kilos por cereal.
    :param precio_cereal: Lista con los precios de los cereales.
    :return: Lista con la recaudación por cereal.
    """
    recaudacion = []
    for i in range(len(sumatoria_columna)):
        recaudacion.append(sumatoria_columna[i] * precio_cereal[i])
    return recaudacion


def calcular_maxima_recaudacion(matriz_cargada, recaudacion):
    """
    Calcula el depósito con la mayor recaudación.

    :param matriz_cargada: La matriz con las existencias cargadas.
    :param recaudacion: Lista con la recaudación por cereal.
    :return: Lista con el depósito con la mayor recaudación.
    """
    mayor_recaudacion = max(recaudacion)
    lista_recaudacion = []

    for i in range(len(recaudacion)):
        if recaudacion[i] == mayor_recaudacion:
            nombre_recaudacion = matriz_cargada[0][i]
            lista_recaudacion.append(nombre_recaudacion)

    return lista_recaudacion if lista_recaudacion else ["Ninguno"]


def calcular_depositos_50000kg(sumatoria_fila):
    """
    Calcula cuántos depósitos han almacenado más de 50,000 kilos.

    :param sumatoria_fila: Lista con la sumatoria de kilos por depósito.
    :return: Cantidad de depósitos con más de 50,000 kilos almacenados.
    """
    contador = 0
    for i in range(len(sumatoria_fila)):
        if sumatoria_fila[i] > 50000:
            contador += 1
    return contador if contador > 0 else "Ninguno de los depositos han almacenado mas de  50000 kg."


def calcular_totales_cereales(matriz_cargada):
    """
    Calcula el total de kilos almacenados por cada cereal en todos los depósitos.
    """
    totales_cereales = {cereal: 0 for cereal in granos_a_utilizar()}
    total_kilos = 0  

    for i in range(1, len(matriz_cargada)):
        for j in range(4):  
            kilos = int(matriz_cargada[i][j])  
            if kilos > 0:  
                cereal = granos_a_utilizar()[j]  
                totales_cereales[cereal] += kilos  
                total_kilos += kilos  

    return totales_cereales, total_kilos

def calcular_porcentajes(totales_cereales, total_kilos):
    """
    Calcula el porcentaje de kilos de cada cereal sobre el total de kilos almacenados.
    """
    porcentajes = {}
    for cereal, cantidad in totales_cereales.items():
        if total_kilos > 0:  
            porcentajes[cereal] = (cantidad / total_kilos) * 100
        else:
            porcentajes[cereal] = 0.0

    return porcentajes

def encontrar_cereal_maximo(porcentajes):
    """
    Encuentra el cereal con el máximo porcentaje.
    """
    cereal_maximo = max(porcentajes, key=porcentajes.get)
    return cereal_maximo, porcentajes[cereal_maximo]

def mostrar_porcentajes_y_maximo(matriz_cargada):
    """
    Muestra el porcentaje de kilos de cada cereal sobre el total de kilos almacenados
    y el cereal con el máximo porcentaje.
    """
    totales_cereales, total_kilos = calcular_totales_cereales(matriz_cargada)
    porcentajes = calcular_porcentajes(totales_cereales, total_kilos)

    cereal_maximo, porcentaje_maximo = encontrar_cereal_maximo(porcentajes)

    print("Porcentaje de kilos de cada cereal sobre el total de kilos almacenados:")
    for cereal, porcentaje in porcentajes.items():
        print(f"{cereal}: {porcentaje:.2f}%")

    print(f"Cereal con el máximo porcentaje: {cereal_maximo}->{porcentaje_maximo:.2f}%")


def calcular_recaudacion_por_deposito(matriz_cargada, precios):
    """
    Calcula la recaudación total por depósito multiplicando las cantidades por los precios.
    """
    recaudaciones = []
    for i in range(1, len(matriz_cargada)): 
        recaudacion = 0
        for j in range(len(matriz_cargada[i])):
            recaudacion += int(matriz_cargada[i][j]) * precios[j]
        recaudaciones.append(recaudacion)
    return recaudaciones

def bubble_sort_recaudaciones(recaudaciones, depositos):
    """
    Ordena las recaudaciones y sus depósitos asociados de mayor a menor
    utilizando el método de ordenamiento Bubble Sort.
    """
    n = len(recaudaciones)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if recaudaciones[j] < recaudaciones[j + 1]:
                recaudaciones[j], recaudaciones[j + 1] = recaudaciones[j + 1], recaudaciones[j]
                depositos[j], depositos[j + 1] = depositos[j + 1], depositos[j]

def generar_informe_recaudaciones(matriz_cargada):
    """
    Genera un informe con la recaudación de cada depósito, ordenada de mayor a menor.
    """
    precios = precios_cereales() 
    recaudaciones = calcular_recaudacion_por_deposito(matriz_cargada, precios)  
    depositos = [f"Depósito {i + 1}" for i in range(len(recaudaciones))]

    bubble_sort_recaudaciones(recaudaciones, depositos)

    print("Informe de recaudaciones (ordenadas de mayor a menor):")
    for i in range(len(recaudaciones)):
        print(f"{depositos[i]}: ${recaudaciones[i]}")

################### MAIN #######################

# MENU DE OPCIONES
def menu_opciones():
    print("Elija una opción dentro del menú:")
    print("==================================")
    print("1. Obtener existencias.")
    print("2. Total de kilos almacenados por depósitos.")
    print("3. Nombre del cereal que almacenó menos kilos en cada depósito.")
    print("4. Máxima cantidad de kilos almacenados de cada cereal.")
    print("5. Depósito con mayor recaudación.")
    print("6. Cantidad de depósitos que hayan almacenado más de 50000 kilos entre los 4 cereales.")
    print("7. Porcentaje de kilos de cada cereal sobre el total de kilos almacenados. Nombre del cereal con el máximo porcentaje.")
    print("8. Informe con la recaudación de cada depósito, ordenada de mayor a menor.")
    print("9. Salir.")

# LLAMADA A LAS FUNCIONES

def creacion_matriz_cereales():
    creacion_matriz = crear_matriz(0, 3, 4)
    granos = granos_a_utilizar()
    estructura_matriz = cargar_primera_linea(creacion_matriz, granos)
    matriz_cargada = cargar_matriz(estructura_matriz)
    return matriz_cargada

def calcular_recaudacion(matriz_cargada):
    precio_cereales = precios_cereales()
    total_cereales = calcular_total_cereales(matriz_cargada) 
    recaudacion_precios = recaudar_cereales(total_cereales, precio_cereales)  
    maxima_recaudacion = calcular_maxima_recaudacion(matriz_cargada, recaudacion_precios)  

# PROGRAMA PRINCIPAL
def programa():
    matriz_cargada = [] 
    granos = granos_a_utilizar()  
    bandera = True

    # Mostrar el menú solo una vez
    menu_opciones()

    while bandera:
        opcion = input("Ingrese su opción: ")

        match opcion:
            case "1":
                matriz_cargada = creacion_matriz_cereales()
                mostrar_matriz(matriz_cargada)  

            case "2":
                if matriz_cargada:
                    sumatoria_fila = calcular_sumatoria_fila(matriz_cargada)
                    mostrar_sumatoria_fila(sumatoria_fila)
                else:
                    print("Primero debe cargar las existencias presionando en 1.")
        
            case "3":
                if matriz_cargada:
                    granos = granos_a_utilizar()
                    granos_minimo = calcular_minimos(matriz_cargada, granos)
                    granos_minimo_formateado = eliminar_duplicados_y_formatear(granos_minimo)

                    print(f"Cereal que almacenó menos kilos en cada depósito: {granos_minimo_formateado}.")

                else:
                    print("Primero debe cargar las existencias presionando en 1.")

            case "4":
                if matriz_cargada:
                    maxima_cantidad_kg(matriz_cargada, granos)
                else:
                    print("Primero debe cargar las existencias presionando el 1.")

            case "5":
                if matriz_cargada:
                    recaudacion = calcular_recaudacion(matriz_cargada)
                    if len(recaudacion) == 1:
                        print(f"Depósito con mayor recaudación: {recaudacion[0]}")
                    else:
                        # Si hay más de un depósito, los mostramos con comas
                        print(f"Depósitos con mayor recaudación: {', '.join(recaudacion)}")
                else:
                    print("Primero debe cargar las existencias presionando el 1.")

            case "6":
                if matriz_cargada:
                    sumatoria_fila = calcular_sumatoria_fila(matriz_cargada)
                    contador_mas_50000 = calcular_depositos_50000kg(sumatoria_fila)
                    print(f"Hay {contador_mas_50000} depositos que almacenaron mas de 50.000kg almacenados.")
                else:
                    print("Primero debe cargar las existencias presionando el 1.")

            case "7":
                if matriz_cargada:
                    mostrar_porcentajes_y_maximo(matriz_cargada)
                else:
                    print("Primero debe cargar las existencias presionando el 1.")

            case "8":
                if matriz_cargada:
                    generar_informe_recaudaciones(matriz_cargada)
                else:
                    print("Primero debe cargar las existencias presionando el 1.")

            case "9":
                print("Gracias por utilizar mi programa!")
                bandera = False

            case _:
                print("Opción inválida. Por favor ingrese una opción del 1 al 9.")

# Ejecutar programa
programa()
