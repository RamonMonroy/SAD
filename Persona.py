class Persona:
    def __init__(self, nombre, edad, correo):
        self.__nombre = nombre
        self.__edad = edad
        self.__correo = correo

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_correo(self):
        return self.__correo

    def mostrar_datos(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"Correo: {self.__correo}")
