class Producto:
    def __init__(self, codigo, nombre, precio):
        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio
    
    # Getters
    def get_codigo(self):
        return self._codigo

    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio
    
    # Setters
    def set_codigo(self, codigo):
        self._codigo = codigo

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_precio(self, precio):
        if precio >= 0:
            self._precio = precio
        else:
            raise ValueError("El precio debe ser un número positivo")
    
    # Calcular el precio total
    def calcular_total(self, unidades):
        if unidades < 0:
            raise ValueError("Las unidades deben ser un número positivo")
        return self._precio * unidades
