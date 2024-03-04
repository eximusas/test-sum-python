

import sys

# Imprime los argumentos pasados al script
print("Argumentos pasados al script:", sys.argv)

# Si se pasaron parámetros, accede a ellos
if len(sys.argv) > 1:
    parametro = sys.argv[1]
    print("El parámetro pasado al script es:", parametro)
else:
    print("No se pasaron parámetros al script.")