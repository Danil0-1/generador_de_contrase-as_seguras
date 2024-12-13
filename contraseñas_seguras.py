bienvenida = print("Bienvenid@ ! :La generación de contraseñas se realiza a través de una función que toma la longitud y las preferencias del usuario y devuelve una contraseña segura.")

longitud=int(input("1.Ingresa la longitud de la contraseña: "))
mayusculas=input("2.Ingresa las mayusculas de la contraseña: ")
minusculas=input("3.Ingresa las minusculas de la contraseña: ")
caracteres_alfanumericos=input("4.Ingresa los caracteres alfanumericos de la contraseña: ")
simbolos=input("5.Ingresa los simbolos de la contraseña: ")

def contraseña(datos):
    print(datos)
print("Contraseña generada: ")
contraseña(mayusculas + minusculas + caracteres_alfanumericos + simbolos)

print("¿Desea generar otra contraseña?: ")
