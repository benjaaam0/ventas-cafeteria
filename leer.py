with open("ventas.txt", "r") as archivo:
    # Leemos el contenido del archivo y lo dividimos por líneas
    lineas = archivo.read().splitlines()

print(lineas)


with open("informe_ventas.txt", "w") as informe:
    # Escribimos el encabezado del informe
    informe.write("Informe de Ventas - Cafetería de Grano\n\n")