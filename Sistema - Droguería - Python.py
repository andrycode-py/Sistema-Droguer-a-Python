#Vamos a crear una lista vacía  llamada "productos" para guardar los productos.
productos = []

#En esta lista vacía se van a guardar las ventas de los productos
ventas = []


#Función para registrar productos
def registrar_productos():

    print("\n==============================================")
    print("        REGISTRAR PRODUCTOS")
    print("================================================")

    #Se piden los datos del producto al empleado
    while True:
        try:
            codigo = int(input("Código del producto: "))
            descripcion = input("Descripción del producto: ").title()
            unidad = input("Unidad - (Individual / Caja / Frasco): ").title()
            if unidad != "Individual" and unidad != "Caja" and unidad != "Frasco":
                print("Ingrese una unidad correcta")
                continue
            break
        except ValueError:
            print("ERROR: Ingrese un número entero")

    #Se pide el costo y el porcentaje de utilidad
    while True:
        try:
            costo = float(input("Costo del producto: "))
            utilidad = float(input("% Utilidad: "))
            break
        except ValueError:
            print("ERROR: Ingrese un número válido")

    #El precio de venta se calcula automáticamente
    precio_venta = costo + (costo * utilidad / 100)
 
    print(f"Precio de venta calculado: ${precio_venta:.2f}")

    #Se pide la cantidad disponible del producto
    while True:
        try:
            existencia = int(input("Existencia inicial: "))
            break
        except ValueError:
            print("ERROR: Ingrese un número entero")

    #Se guarda el producto en el diccionario
    producto = {

        "codigo": codigo,
        "descripcion": descripcion,
        "unidad": unidad,
        "costo": costo,
        "utilidad": utilidad,
        "precio de venta": precio_venta,
        "existencia": existencia
    }

    #Se guarda el producto en la lista productos
    productos.append(producto)

    print("¡Producto registrado exitosamente!")


#Función para vender productos
def venta_productos():

    print("\n==============================================")
    print("                 VENTA DE PRODUCTOS")
    print("=========================================")

    #Se piden los datos del pedido
    while True:
        try:
            numero_pedido = int(input("Número de pedido: "))
            break
        except ValueError:
            print("ERROR: Ingrese un número entero")

    nombre_cliente = input("Nombre del cliente: ").title()

    #Tipo de venta
    while True:
        print("\nTipo de venta")
        print("1. Mostrador")
        print("2. Domicilio")
        tipo_venta = input("Seleccione el tipo de venta (1 o 2): ")

        if tipo_venta == "1" or tipo_venta == "2":
            break
        print("Valor incorrecto. Intente de nuevo.")

    if tipo_venta == "2":
        direccion = input("Ingrese la direccion de envio: ").capitalize()
    else:
        direccion = "N/A"

    #Forma de pago
    while True:
        print("\nForma de pago")
        print("1. Efectivo")
        print("2. Transferencia")
        forma_pago = input("Seleccione la forma de pago (1 o 2): ")

        if forma_pago == "1" or forma_pago == "2":
            break
        print("Valor incorrecto. Intente de nuevo.")

    if forma_pago == "1":
        forma_pago = "Efectivo"
    else:
        forma_pago = "Transferencia"

    #Buscar producto
    while True:
        try:
            codigo = int(input("Ingrese el código del producto: "))
            break
        except ValueError:
            print("ERROR: Ingrese un número entero")
    
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            break
        except ValueError:
            print("ERROR: Ingrese un número entero")

    encontrado = False

    #Recorrer la lista productos
    for p in productos:

        if p["codigo"] == codigo:

            encontrado = True

            #Validar existencia
            if cantidad > p["existencia"]:

                print("ERROR: La cantidad supera la existencia.")

            else:

                #Descontar existencia
                p["existencia"] -= cantidad

                #Calcular total
                total = cantidad * p["precio de venta"]

                #Guardar venta
                venta = {

                    "numero de pedido": numero_pedido,
                    "cliente": nombre_cliente,
                    "tipo de venta": tipo_venta,
                    "direccion": direccion,
                    "forma de pago": forma_pago,
                    "producto": p["descripcion"],
                    "unidad": p["unidad"],
                    "cantidad": cantidad,
                    "precio de venta": p["precio de venta"],
                    "total": total,
                    "estado": "pendiente"
                }

                ventas.append(venta)

                print(f"¡Venta registrada! Total: ${total:.2f}")

    #Si no encuentra el producto
    if not encontrado:

        print("Producto no encontrado")


#Función para ver productos
def ver_productos():

    print("\n==============================================")
    print("           VER PRODUCTOS")
    print("================================================")

    if len(productos) == 0:
        print("No hay productos registrados.")
        return

    print(f"\n{'Código':<10} {'Descripción':<20} {'Unidad':<12} {'Precio':<12} {'Existencia':<10}")
    print("-" * 60)
    for p in productos:
        print(f"{p['codigo']:<10} {p['descripcion']:<20} {p['unidad']:<12} ${p['precio de venta']:<11.2f} {p['existencia']:<10}")


#Función para facturar pedidos
def facturar_pedido():

    print("\n==============================================")
    print("           FACTURAR PEDIDO")
    print("================================================")

    #Se pide el número de pedido
    while True:
        try:
            numero = int(input("Ingrese el número de pedido: "))
            break
        except ValueError:
            print("ERROR: Ingrese un número entero")

    encontrado = False

    #Recorrer ventas
    for v in ventas:

        if v["numero de pedido"] == numero:

            encontrado = True

            if v["estado"] != "Facturado":
                v["estado"] = "Facturado"
                print("Pedido facturado correctamente.")
            else:
                print("El pedido ya estaba facturado.")

            #Mostrar datos
            print(f"\nCliente: {v['cliente']}")
            print(f"Direccion: {v['direccion']}")
            print(f"Producto: {v['producto']}")
            print(f"Cantidad: {v['cantidad']}")
            print(f"Total: {v['total']}")
            print(f"Estado: {v['estado']}")

    #Si no encuentra el pedido
    if not encontrado:

        print("Pedido no encontrado")


#Función para ver el estado de cuenta
def estado_cuenta():

    print("\n==============================================")
    print("           ESTADO DE CUENTA")
    print("================================================")

    if len(ventas) == 0:
        print("No hay ventas registradas.")
        return

    #Contadores para domicilio y mostrador
    total_domicilio = 0
    total_mostrador = 0

    print("\n--- RELACIÓN DE PEDIDOS ---")
    print(f"\n{'No.Pedido':<12} {'Cliente':<18} {'Producto':<18} {'Cantidad':<10} {'Total':<12} {'Estado':<12} {'Tipo':<12}")
    print("-" * 90)

    for v in ventas:
        print(f"{v['numero de pedido']:<12} {v['cliente']:<18} {v['producto']:<18} {v['cantidad']:<10} ${v['total']:<11.2f} {v['estado']:<12} {v['tipo de venta']:<12}")

        if v["tipo de venta"] == "2":
            total_domicilio += v["total"]
        else:
            total_mostrador += v["total"]

    print("\n--- VENTAS POR TIPO ---")
    print(f"Ventas por domicilio:  ${total_domicilio:.2f}")
    print(f"Ventas por mostrador:  ${total_mostrador:.2f}")
    print(f"Total general:         ${total_domicilio + total_mostrador:.2f}")




#Función del menú principal
def menu_principal():

    print("\n=================================================")
    print("        SISTEMA DE PEDIDOS - FARMA NEL")
    print("=================================================")

    print("1. Registrar productos")
    print("2. Venta de productos")
    print("3. Facturar pedidos")
    print("4. Ver productos")
    print("5. Estado de cuenta")
    print("6. Salir")


#Menú 
while True:

    menu_principal()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        registrar_productos()

    elif opcion == "2":

        venta_productos()

    elif opcion == "3":

        facturar_pedido()

    elif opcion == "4":

        ver_productos()

    elif opcion == "5":

        estado_cuenta()

    elif opcion == "6": 
        print("Saliendo del programa...")
        break 

    else:

        print("Opción no válida, inténtelo de nuevo.")
