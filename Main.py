
from Estudiante import Estudiante
from Profesor import Profesor
from Curso import Curso

def main():
    # Crear cursos
    curso1 = Curso("Programación Orientada a Objetos", "POO101", 6)
    curso2 = Curso("Estructuras de Datos", "ED202", 5)

    # Crear estudiante
    estudiante = Estudiante("Luis García", 20, "luis.garcia@uni.edu", "A01234567")

    estudiante2 = Estudiante ("Ricardo Garcia", 22, "Elpaponas22.@uni.edu", "A01234568")
    
    # Crear profesor
    profesor = Profesor("Dra. Ana Pérez", 45, "ana.perez@uni.edu", "Ingeniería de Software")

    # Inscribir estudiante en dos cursos
    estudiante.inscribir_curso(curso1)
    estudiante.inscribir_curso(curso2)
    estudiante2.inscribir_curso(curso1)
    # Asignar un curso al profesor
    profesor.asignar_curso(curso1)

    # Mostrar información
    print("\n--- Datos del Estudiante ---")
    estudiante.mostrar_datos()
    estudiante.mostrar_cursos()
    estudiante2.mostrar_cursos()
    estudiante2.mostrar_datos()
    print("\n--- Datos del Profesor ---")
    profesor.mostrar_datos()
    profesor.mostrar_asignaciones()

    print("\n--- Descripción de los Cursos ---")
    print(curso1.descripcion())
    print(curso2.descripcion())


if __name__ == "__main__":
    main()
