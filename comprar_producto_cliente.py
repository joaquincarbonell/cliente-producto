class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


def comprar_producto_cliente(cliente, producto, unidades):
    print(
        f"El cliente con nombre {cliente.nombre} "
        f"ha comprado el producto con nombre {producto.nombre} "
        f"por un precio unitario de {producto.precio} € "
        f"y un total de {unidades} unidades."
    )


cliente1 = Cliente("Joaquin", "joaquin@gmail.com")
producto1 = Producto("Auriculares", 79.99)

comprar_producto_cliente(cliente1, producto1, 2)