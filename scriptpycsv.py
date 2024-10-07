import csv

def procesar_csv(ruta_archivo):
    nuevas_filas = []
    with open(ruta_archivo, mode='r', encoding='latin-1') as archivo:
        lector = csv.reader(archivo, delimiter=';')
        for fila in lector:
            nueva_fila = [elemento.replace(';', '""') for elemento in fila]
            # Si el último elemento está vacío, agregar ';;' al final de la línea
            if nueva_fila[-1] == '':
                nueva_fila[-1] = ';;'
            nuevas_filas.append(nueva_fila)

    # Escribir en el archivo de salida
    with open('archivo_procesado1.csv', mode='w', encoding='latin-1', newline='') as archivo:
        escritor = csv.writer(archivo, delimiter=';')
        escritor.writerows(nuevas_filas)  # Escribir todas las nuevas filas

# Llama a la función con el archivo que deseas procesar
procesar_csv('02-10-2024.csv')