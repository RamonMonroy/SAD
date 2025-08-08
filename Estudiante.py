from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, correo, matricula):
        super().__init__(nombre, edad, correo)
        self.__matricula = matricula
        self.__cursos_inscritos = []

    def inscribir_curso(self, curso):
        self.__cursos_inscritos.append(curso)

    def mostrar_cursos(self):
        print(f"Cursos inscritos por el estudiante {self.get_nombre()}:")
        if not self.__cursos_inscritos:
            print("No hay cursos inscritos.")
        for curso in self.__cursos_inscritos:
            print(f"- {curso.nombre}")
