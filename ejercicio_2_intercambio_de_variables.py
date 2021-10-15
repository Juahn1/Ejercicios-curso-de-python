#intercambiar valores   a =30       b=30
#                       b = 20      a=20

def intercambiar_valores(a,b):
    a,b=b,a
    print(f"El valor a = {a} fue intercambiado con el valor b = {b} ")


a = float(input("ingrese el valor A : "))
b = float(input("ingrese el valor B : "))

print ("")
print ("")
print ("Intercambiando valores... \n")
print ("")
print ("")

intercambiar_valores(a,b)