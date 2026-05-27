# DIEGO FERNANDO ECHEVERRIA 
# c.c 1049605957
# FASE 5 EJERCICIO 5


# Definimos la matriz: [Nombre del recurso, Lun, Mar, Mié, Jue, Vie]
matriz_trabajo = [
    ["Diego", 8, 6, 4, 8, 2],
    ["Fernando", 8, 7, 8, 7, 10],
    ["Juan", 5, 10, 9, 9, 8],
    ["Pedro", 5, 8, 8, 7, 7],
    ]

UMBRAL_HORAS = 40

print(f"{'Nombre':<10} | {'Total':<7} | {'Estado'}")
print("-" * 35)

for fila in matriz_trabajo:
    nombre = fila[0]
    # Sumamos las horas (desde el índice 1 al final)
    total_horas = sum(fila[1:])
    
    # Verificación de exceso
    excedido = "SOBRETIEMPO" if total_horas > UMBRAL_HORAS else "HORARIO STANDARD"
    
    print(f"{nombre:<10} | {total_horas:<7} | {excedido}")