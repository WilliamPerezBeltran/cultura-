import re

palabra_objetivo = "Javi"  # Cambia esto por la palabra que buscas

with open("jose.txt", "r") as f:
    contenido = f.read()

# Expresión regular para agregar un salto de línea antes de la palabra (sin modificar el archivo)
nuevo_contenido = re.sub(rf"(?<!\n)({palabra_objetivo})", r"\n\n\1", contenido)

print(nuevo_contenido)  # Muestra el texto con el salto de línea antes de la palabra

