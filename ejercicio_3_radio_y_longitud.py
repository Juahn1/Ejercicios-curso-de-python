import math
try:
    r= float(input("Ingrese el radio:  "))
    def area_y_longitud(r):    
        area = math.pi*(r**2)
        longitud = 2*math.pi*r
        print(f"El area es {area:.4f} y la longitud es {longitud:.4f}")
    print("")
    area_y_longitud(r)
    print("")
    
except:
    ValueError
    print("Ingrese un numero valido")
