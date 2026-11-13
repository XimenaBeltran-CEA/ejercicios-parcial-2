nombre =[]
categoria = []
cantidad = 0
fechaIngreso = []
codigo = []
precio = 0.0
opcion = 0
 
print("Bienvenido al sistema de registro de artículos")
print("---------MENÚ PRINCIPAL---------")
print("1. Registrar artículo")
print("2. Ver información del artículo")
print("3. Borrar información del artículo")
print ("4. Modificar información del artículo")
print("5. Salir")
print("---------------------------------")
opcion = int(input("Selecciona una opción: "))
 
match opcion:#Aquí inicia el match, que es una validación de caso
   
    case 1:
        nombre = input("Ingresa el nombre del artículo: ")
        categoria = input("Ingresa la categoría del artículo: ")
        cantidad = int(input("Ingresa la cantidad disponible: "))
        fechaIngreso = input("Ingresa la fecha de ingreso: ")
        codigo = input("Ingresa el código del artículo: ")
        precio = float(input("Ingresa el precio del artículo: "))
    case 2:
        print("Nombre:", nombre, "Categoría:", categoria, "Cantidad:", cantidad, "Fecha de ingreso:", fechaIngreso, "Código:", codigo, "Precio:", precio)
    case 3:
        nombre = ""
        categoria = ""
        cantidad = 0
        fechaIngreso = ""
        codigo = ""
        precio = 0.0
    case 4:
        nombre.append (input("Ingresa el nuevo nombre del artículo: "))
        categoria.append(input("Ingresa la nueva categoría del artículo: ")
        cantidad .append(int(input("Ingresa la nueva cantidad disponible: "))
        fechaIngreso.append(input("Ingresa la nueva fecha de ingreso: "))
        codigo = input("Ingresa el nuevo código del artículo: ")
        precio = float(input("Ingresa el nuevo precio del artículo: "))
    case 5:
        print("¡Hasta luego!")
    case _:
        print("Opción no válida")