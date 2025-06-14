
# --- PARTE 2: DESARROLLO DEL PROGRAMA EN PYTHON ---

# Ingreso de DNIs (pueden ser modificados por otros)
dnis = [35966752, 42469802, 42561321]

# Generación automática de conjuntos de dígitos únicos
conjuntos_digitos = [set(str(dni)) for dni in dnis]
print("Conjuntos de dígitos únicos:")
for i, conj in enumerate(conjuntos_digitos):
    print(f"Conjunto {i+1}: {conj}")

# Operaciones entre los conjuntos
union = conjuntos_digitos[0] | conjuntos_digitos[1] | conjuntos_digitos[2]
interseccion = conjuntos_digitos[0] & conjuntos_digitos[1] & conjuntos_digitos[2]
diferencia_01 = conjuntos_digitos[0] - conjuntos_digitos[1]
diferencia_12 = conjuntos_digitos[1] - conjuntos_digitos[2]
dif_sim_01 = conjuntos_digitos[0] ^ conjuntos_digitos[1]
dif_sim_12 = conjuntos_digitos[1] ^ conjuntos_digitos[2]

print("\nOperaciones:")
print(f"Unión: {union}")
print(f"Intersección: {interseccion}")
print(f"Diferencia (0 - 1): {diferencia_01}")
print(f"Diferencia (1 - 2): {diferencia_12}")
print(f"Diferencia Simétrica (0 ^ 1): {dif_sim_01}")
print(f"Diferencia Simétrica (1 ^ 2): {dif_sim_12}")

# Frecuencia de cada dígito por DNI
print("\nFrecuencia de dígitos por DNI:")
for dni in dnis:
    frecuencia = {str(d): str(dni).count(str(d)) for d in range(10) if str(dni).count(str(d)) > 0}
    print(f"DNI {dni}: {frecuencia}")

# Suma total de los dígitos de cada DNI
print("\nSuma total de los dígitos por DNI:")
for dni in dnis:
    suma = sum(int(d) for d in str(dni))
    print(f"DNI {dni}: {suma}")

# Evaluación de condiciones lógicas
print("\nEvaluaciones lógicas:")
if interseccion:
    print("Dígito compartido:", interseccion)
for i, conj in enumerate(conjuntos_digitos):
    if len(conj) > 6:
        print(f"Conjunto {i+1} tiene diversidad numérica alta.")

# --- OPERACIONES CON AÑOS DE NACIMIENTO ---
anios_nacimiento = [2002, 2003, 1999]  # ejemplo
edades_actuales = [2025 - anio for anio in anios_nacimiento]

pares = sum(1 for anio in anios_nacimiento if anio % 2 == 0)
impares = len(anios_nacimiento) - pares
print(f"\nCantidad de años pares: {pares}, impares: {impares}")

if all(anio > 2000 for anio in anios_nacimiento):
    print("Grupo Z")
if any((anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)) for anio in anios_nacimiento):
    print("Tenemos un año especial")

# Función para determinar si un año es bisiesto
def es_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

print("\nAños bisiestos detectados:")
for anio in anios_nacimiento:
    if es_bisiesto(anio):
        print(f"{anio} es bisiesto")

# Producto cartesiano entre años y edades
producto_cartesiano = [(a, e) for a in anios_nacimiento for e in edades_actuales]
print("\nProducto cartesiano (Años x Edades):")
for par in producto_cartesiano:
    print(par)
