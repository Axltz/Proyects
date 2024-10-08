#Sistema de Inventario para tienda
import os

Lista_Productos = []


def Mostrar_Main_Menu():
  while True:
    print("***************************")
    print("*-Gestor de negocio v1.0.-*")
    print("***************************")

    print("Bienvenido, seleccione una opción por favor.")
    print("\n\t1. Gestor del inventario.\n\t0. Salir del programa")
    while True:
      seleccion = input("Elección: ")
      if seleccion == "1":
         os.system("cls")
         Menu_Gestor_Inventario()
         break
      elif seleccion == "0":
         print("Saliendo del programa...")
         break
      else: 
         print("Opción no valida, selecciona una opción existente!")

    if seleccion == "0":
      confirm = input("¿Estás seguro de que deseas salir? (si/no): ").lower()
      if confirm == "si":
          os.system('cls')
          break  
      elif confirm == "no":
          os.system("cls")
          continue  
      else:
          print("Opción no válida, por favor ingresa 'si' o 'no'.")
def Menu_Gestor_Inventario(): 
  while True: 
      print("Has ingresado al gestor del inventario\n")
      print("Por favor seleccione una opción:")
      print("\n\t1. Agregar producto.\n\t2. Editar producto existente.\n\t3. Eliminar producto.\n\t0. Salir\n")
      seleccion = int(input("Elección: "))
      if seleccion == 1:
         os.system("cls") 
         Agregar_Producto()
         os.system("cls")
      elif seleccion == 2:
         os.system("cls")
         Editar_Producto()
         os.system("cls") 
      elif seleccion == 3:
         os.system("cls")         
         Eliminar_Producto()
         os.system("cls") 
      elif seleccion == 0:  
         confirm = input("¿Estás seguro de que deseas salir? (si/no): ").lower()
         if confirm == "si":
           os.system('cls')         
           break
      else: print("Opcion no valida, ingresa una existente.")

def Mostrar_Productos():
    if not Lista_Productos:
      print("No hay productos en el inventario!")
    else:
      print("Listado de productos")
      for i, producto in enumerate(Lista_Productos, start=1):
        print(f"{i}. {producto['nombre']} - Precio por unidad: ${producto['precio']:.2f}, Cantidad: {producto['stock']} unidades")  
def Agregar_Producto():    
        while True:
          print("Has seleccionado agregar un producto.\n")
          Mostrar_Productos()
          producto = input("Ingresa el nombre del producto: ")  
          precio = validar_precio()
          stock = validar_stock()                      
          
          dic_producto = {
          "nombre": producto,
          "stock": stock,
          "precio": precio} 
            
          Lista_Productos.append(dic_producto)
          print("Actualizando inventario...\n")
          print(f"Producto '{dic_producto['nombre']}' fue agregado exitosamente con {dic_producto['stock']} unidades en stock a un precio de ${dic_producto['precio']} por unidad.")

        
          while True:
           print("Esta es la lista actualizada: ")
           Mostrar_Productos()
           seleccion = input("¿Deseas agregar algún otro producto? si/no\n").lower()
           if seleccion == "no":
              print("Saliendo de la opción...")
              break
           elif seleccion == "si":
              break
           else:
              print("Opcion no valida, intente de nuevo")
          if seleccion == "no":   
            break        
def validar_precio():
   while True:
           try:
             precio = float(input("Ingresa el precio por unidad: "))
             if precio > 0:
               return precio
             else:
               print("El precio debe ser mayor a 0.")  
           except ValueError:
              print("Debes ingresar un número válido.") 
def validar_stock():
   while True:
             try:
              stock = int(input("Ingresa la cantidad a agregar: "))  
              if stock > 0:
                return stock
              else:
                print("El stock debe ser mayor a 0.")  
             except ValueError:
                print("Debes ingresar un número válido.") 

def Editar_Producto():
    while True:
        print("Has seleccionado editar el inventario. ")     
        print("¿Qué producto deseas editar?")
        if not Lista_Productos:
           print("Error, no hay productos en el inventario, saliendo de la opción...")
           break
        Mostrar_Productos()
        seleccion = int(input("Elección: ")) -1
        
        if seleccion < 0 or seleccion >= len(Lista_Productos):
            print("Selección inválida.")
            continue
        
        producto = Lista_Productos[seleccion]  
        
        print("¿Qué deseas hacer? \n")
        print("\t1. Actualizar nombre.\n\t2. Actualizar stock.\n\t3. Actualizar precio.")
        accion = int(input("Acción: "))
        
        if accion == 1: 
            producto['nombre'] = input("Ingresa el nuevo nombre del producto: ")
            print("Nombre actualizado exitosamente!")
        elif accion == 2:
            producto['stock'] = int(input("Ingresa el stock disponible: ")) 
            print("Stock actualizado exitosamente!")
        elif accion == 3:
            producto['precio'] = float(input("Ingresa el precio nuevo: ")) 
            print("Precio actualizado exitosamente!")
        else:
            print("Opción no válida.")
            continue

        print("Actualizando inventario...\n")
        print(f"Producto '{producto['nombre']}' fue editado exitosamente con {producto['stock']} unidades en stock a un precio de ${producto['precio']} por unidad.")

        while True:
          print("Esta es la lista actualizada: ")
          Mostrar_Productos()
          seleccion = input("¿Deseas editar algún otro producto? si/no\n").lower()
          if seleccion == "no":
              break
          elif seleccion == "si":
              break
          else:
              print("Opción no válida, intente de nuevo")
        if seleccion == "no":
         break 
def Eliminar_Producto():
  while True:
    print("Has seleccionado eliminar producto")
    print("¿Qué producto deseas eliminar?")
    Mostrar_Productos()
    seleccion = int(input("Elección: ")) - 1
    if seleccion < 0 or seleccion >= len(Lista_Productos):
       print("Opción no existente, ingresa una opción valida.")

    if confirmar_accion(f"¿Estas seguro de eliminar el producto {Lista_Productos[seleccion]['nombre']}? (si/no): "):
      del Lista_Productos[seleccion]
      print("Eliminando producto...")
      print("Aplicando cambios..")
      print("Producto eliminado correctamente!")
      print("Lista actualizada:\n")
      Mostrar_Productos()
    while True: 
      print("Deseas eliminar algún otro? si/no")
      seleccion = input()
      if seleccion == "si":
         break
      elif seleccion == "no":
         break
      else:
         print("Opción no valida, intenta otra vez.")
    if seleccion == "no":
       break
def confirmar_accion(mensaje):
    while True:
        confirmacion = input(mensaje).lower()
        if confirmacion in ["si", "no"]:
            return confirmacion == "si"
        else:
            print("Opción no válida, intenta de nuevo.")
if __name__ == "__main__":
   Mostrar_Main_Menu()