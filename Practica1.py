# Práctica 1
# Implementa el cálculo del área y el perímetro de
# un círculo, dado un radio r, según las fórmulas
# área = π * r^2 y perímetro = 2 * π * r.
print("\n")
print("Ejercicio 1.")
radio = float(input("Introduce el radio: "))


def area(r):
    return 3.14 * r * r


def perimetro(r):
    return 2 * 3.14 * r


print(f"Área: {area(radio)}")
print(f"Perímetro: {perimetro(radio)}")

# ---------------------------------------------------------------------------
# ¿Qué variables son de entrada, qué variables son de salida,
# y cuáles auxiliares?

# Variables de entrada: en la función area, la variable de entrada es r.
# En la función perímetro, la variable de entrada es r también. En ambas,
# la variable de salida es una función (a operación)
# ---------------------------------------------------------------------------
# ¿Se pueden declarar constantes en Python, como por ejemplo PI?
# ---------------------------------------------------------------------------
# ¿Por qué ponemos un conversor de tipo (“float”) delante de la
# entrada de datos (“input”)?
#
# ¿Qué pasaría si no?
print("\n")
print("Ejercicio 2.")

# ---------------------------------------------------------------------------
print("\n")
print("Ejercicio 3.")


# Crea un programa llamado ex_2_2, que pida tres notas y calcule la media.

def ex_2_2_(a, b, c):
    return (a + b + c) / 3


# ---------------------------------------------------------------------------
print("\n")
print("Ejercicio 4.")


# Crea un programa llamado ex_2_4, que dado un número entero que designa un
# periodo de tiempo expresado en segundos, imprima el equivalente en días, horas,
# minutos y segundos.
# Por ejemplo: 300000 segundos serán 3 días, 11 horas, 20 minutos y 0 segundos.
# Por ejemplo: 7400 segundos serán 0 días, 2 horas, 3 minutos y 20 segundos.

def ex_2_4(a):
    # dias
    horas = a / 3600
    minutos = a / 60
    # segundos
    return 0


# ---------------------------------------------------------------------------
print("\n")
print("Ejercicio 5.")


# Crea un programa llamado ex_2_5, que dado el PID de un proceso recibido por
# línea de comandos, imprima:
# a) información relevante de dicho proceso, y
# b) dónde se encuentra el archivo ejecutable.
# Pistas: juega con subprocess.check_output() o con psutil.Process()

def ex_2_5(a):
    return 0


# ---------------------------------------------------------------------------
print("\n")
print("Ejercicio 6.")


# Abre un terminal y observa los puertos abiertos con el comando ss -penta.
# A continuación crea un programa llamado ex_2_6 que analice un puerto TCP
# abierto y otro cerrado.

def ex_2_6():
    return 0

# ---------------------------------------------------------------------------
