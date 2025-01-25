class Pedido:
    def __init__(self):
        self._productos = []
        self._cantidades = []

    def agregar_producto(self, producto, cantidad):
        if not isinstance(producto, Producto):
            raise TypeError("El objeto debe ser una instancia de la clase Producto")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser un número positivo")
        
        self._productos.append(producto)
        self._cantidades.append(cantidad)

    def total_pedido(self):
        total = 0
        for producto, cantidad in zip(self._productos, self._cantidades):
            total += producto.calcular_total(cantidad)
        return total

    def mostrar_productos(self):
        for producto, cantidad in zip(self._productos, self._cantidades):
            print(f"{producto.get_nombre()} (Código: {producto.get_codigo()}): {cantidad} unidades - Precio por unidad: {producto.get_precio()} - Subtotal: {producto.calcular_total(cantidad)}")
