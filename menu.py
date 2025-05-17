from proveedores import Proveedor
from productos import Producto

proveedor1 = None

def menu():
    global proveedor1
    while True:
        print("\n===== MENÚ DE PROVEEDORES Y PRODUCTOS =====")
        print("1. Agregar Proveedor")
        print("2. Crear Producto")
        print("3. Agregar Producto al Proveedor")
        print("4. Listar Productos del Proveedor")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            proveedor1 = Proveedor()
            apellidos = input("Ingrese apellidos del proveedor: ")
            nombre = input("Ingrese nombre del proveedor: ")
            telefono = input("Ingrese teléfono: ")
            proveedor1.agregar_proveedor(apellidos, nombre, telefono)
            print("Proveedor registrado correctamente.")

        elif opcion == '2':
            if proveedor1 is None:
                print("Primero debe ingresar un proveedor.")
                continue
            codigo = input("Ingrese código del producto: ")
            nombre_prod = input("Ingrese nombre del producto: ")
            precio = float(input("Ingrese precio del producto: "))
            producto = Producto(codigo, nombre_prod, precio)
            print("Producto creado. Use la opción 3 para agregarlo al proveedor.")

        elif opcion == '3':
            if proveedor1 is None:
                print("Primero debe registrar un proveedor.")
                continue
            try:
                proveedor1.agregar_producto(producto)
                print("Producto agregado al proveedor.")
            except NameError:
                print("Primero debe crear un producto con la opción 2.")

        elif opcion == '4':
            if proveedor1 is None:
                print("No hay proveedor registrado.")
                continue
            print(f"\nProveedor: {proveedor1.mostrar_datos()}")
            print("Productos asociados:")
            print(proveedor1.listar_productos())

        elif opcion == '5':
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

menu()

