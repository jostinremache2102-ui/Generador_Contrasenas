import random
import string

def generar_contrasena(longitud, usar_mayusculas, usar_numeros, usar_simbolos):
    caracteres = string.ascii_lowercase

    if usar_mayusculas:
        caracteres += string.ascii_uppercase

    if usar_numeros:
        caracteres += string.digits

    if usar_simbolos:
        caracteres += string.punctuation

    contrasena = ""

    for i in range(longitud):
        contrasena += random.choice(caracteres)

    return contrasena
def evaluar_seguridad(contrasena):

    nivel = 0

    if len(contrasena) >= 8:
        nivel += 1

    if any(c.isupper() for c in contrasena):
        nivel += 1

    if any(c.isdigit() for c in contrasena):
        nivel += 1

    if any(c in string.punctuation for c in contrasena):
        nivel += 1

    if nivel <= 2:
        return "BAJA"

    elif nivel == 3:
        return "MEDIA"

    else:
        return "ALTA"
print("===================================")
print(" GENERADOR SEGURO DE CONTRASEÑAS ")
print("===================================")

longitud = int(input("Ingrese la longitud de la contraseña: "))

if longitud < 8:
    print("Error: la contraseña debe tener mínimo 8 caracteres.")
else:
    mayusculas = input("¿Desea incluir mayúsculas? (s/n): ")
    numeros = input("¿Desea incluir números? (s/n): ")
    simbolos = input("¿Desea incluir símbolos? (s/n): ")

    usar_mayusculas = mayusculas.lower() == "s"
    usar_numeros = numeros.lower() == "s"
    usar_simbolos = simbolos.lower() == "s"

    contrasena = generar_contrasena(
        longitud,
        usar_mayusculas,
        usar_numeros,
        usar_simbolos
    

    print("-----------------------------------")
    print("Contraseña generada:", contrasena)
    print("-----------------------------------")
    nivel = evaluar_seguridad(contrasena)

print("Nivel de seguridad de la contraseña:", nivel)
