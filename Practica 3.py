#Creamso una funcion que nos da el numero de decadas
print("dime un numero del 10 al 100")
def Decadas(dato):
  #print("Numero de decadas " + dato [0])
  #Funcion mejorada
  if type(dato) is int:
    #No podemos obtener numero de decadas
    #Usando dato [0]
    NumeroDeDecadas = 10
    #Si el año es 58 aplanamos el resultado a entero
    Decadas = int(dato / NumeroDeDecadas)
    print("Numero de decadas " + Decadas)

#Practica 3
nombre = "Miguel"

#En python poder identificar los tipos de datos
#En la siguiente linea se identifica y muestra el tipo
print(type(nombre))

age = 21
#Se comprueba de tipo de edad
print(type(age))

#Pedimos que el usuario nos indidque su nombre
PedirNombre = input("Cual es tu Nombre")
print(type(PedirNombre))
PedirAge = input("Cual es tu Edad")
print(type(PedirAge))

print("Hola " + PedirNombre)
print("Tu inicial es " + PedirNombre[0] )
print("Tu nombre en mayusculas es: " + PedirNombre.upper())
Decadas(PedirAge)


