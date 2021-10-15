#pasar la ecuacion a una expresion algoritmica  (c + 5)(b ^2 -3ac)a^2
#                                                ------------------
#                                                       4a
def ecuacion(a,b,c):
    x=((c+5)*((b**2)-3*a*c)*(a**2))/(4*a)
    print(f"El resultado es {x}")
try:
    a=float(input("Ingrese la variable A: "))
    b=float(input("Ingrese la variable B: "))
    c=float(input("Ingrese la variable C: "))


    ecuacion(a,b,c)
except:
    ValueError
    print("Ingrese un numero valido")