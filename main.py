"""Aplicación básica para registrar y consultar estudiantes.

El proyecto fue creado como práctica inicial de Git y GitHub.
No necesita librerías externas y guarda la información en un archivo JSON.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

DATA_FILE = Path(__file__).parent / "data" / "estudiantes.json"


def cargar_estudiantes() -> list[dict[str, Any]]:
    """Devuelve los estudiantes guardados o una lista vacía."""
    if not DATA_FILE.exists():
        return []

    try:
        contenido = DATA_FILE.read_text(encoding="utf-8")
        datos = json.loads(contenido)
        return datos if isinstance(datos, list) else []
    except (OSError, json.JSONDecodeError):
        print("No se pudo leer el archivo de datos. Se continuará con una lista vacía.")
        return []


def guardar_estudiantes(estudiantes: list[dict[str, Any]]) -> None:
    """Guarda la lista de estudiantes en formato JSON."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(
        json.dumps(estudiantes, ensure_ascii=False, indent=4),
        encoding="utf-8",
    )


def pedir_texto(mensaje: str) -> str:
    """Solicita un texto y evita que se guarde vacío."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("El dato no puede quedar vacío.")
def pedir_matricula(mensaje: str) -> str:
    """Solicita una matrícula válida formada únicamente por números."""
    while True:
        matricula = input(mensaje).strip()

        if matricula.isdigit():
            return matricula

        print("Matrícula no válida. Ingrese únicamente números.")
def encontrar_estudiante_por_matricula(
    estudiantes: list[dict[str, Any]], matricula: str
) -> dict[str, Any] | None:
    """Busca un estudiante por su matrícula."""
    for estudiante in estudiantes:
        if estudiante["matricula"] == matricula:
            return estudiante

    return None
def registrar_estudiante(estudiantes: list[dict[str, Any]]) -> None:
    """Registra un estudiante si la matrícula todavía no existe."""
    matricula = pedir_matricula("Matrícula: ")

    if any(estudiante["matricula"].lower() == matricula.lower() for estudiante in estudiantes):
        print("Ya existe un estudiante con esa matrícula.")
        return

    nuevo_estudiante = {
        "matricula": matricula,
        "nombre": pedir_texto("Nombre completo: "),
        "carrera": pedir_texto("Carrera: "),
        "correo": pedir_texto("Correo electrónico: "),
    }

    estudiantes.append(nuevo_estudiante)
    guardar_estudiantes(estudiantes)
    print("Estudiante registrado correctamente.")


def listar_estudiantes(estudiantes: list[dict[str, Any]]) -> None:
    """Muestra todos los estudiantes registrados."""
    if not estudiantes:
        print("Todavía no existen estudiantes registrados.")
        return

    print("\nESTUDIANTES REGISTRADOS")
    print("-" * 70)
    for numero, estudiante in enumerate(estudiantes, start=1):
        print(f"{numero}. {estudiante['nombre']}")
        print(f"   Matrícula: {estudiante['matricula']}")
        print(f"   Carrera: {estudiante['carrera']}")
        print(f"   Correo: {estudiante['correo']}")
        print("-" * 70)


def editar_estudiante(estudiantes: list[dict[str, Any]]) -> None:
    """Permite modificar la información de un estudiante registrado."""
    matricula = pedir_texto("Ingrese la matrícula del estudiante a editar: ")

    estudiante = encontrar_estudiante_por_matricula(estudiantes, matricula)

    if estudiante is None:
        print("No se encontró un estudiante con esa matrícula.")
        return

    print("\nEstudiante encontrado.")
    print("Ingrese los nuevos datos:")

    estudiante["matricula"] = pedir_matricula("Nueva matrícula: ")
    estudiante["nombre"] = pedir_texto("Nuevo nombre completo: ")
    estudiante["carrera"] = pedir_texto("Nueva carrera: ")
    estudiante["correo"] = pedir_texto("Nuevo correo electrónico: ")

    guardar_estudiantes(estudiantes)
    print("Información actualizada correctamente.")

    listar_estudiantes(resultados)
def editar_estudiante(estudiantes: list[dict[str, Any]]) -> None:
    """Permite modificar la información de un estudiante registrado."""
    matricula = pedir_texto("Ingrese la matrícula del estudiante a editar: ")

    for estudiante in estudiantes:
        if estudiante["matricula"].lower() == matricula.lower():
            print("\nEstudiante encontrado.")
            print("Ingrese los nuevos datos:")

            estudiante["matricula"] = pedir_matricula("Nueva matrícula: ")
            estudiante["nombre"] = pedir_texto("Nuevo nombre completo: ")
            estudiante["carrera"] = pedir_texto("Nueva carrera: ")
            estudiante["correo"] = pedir_texto("Nuevo correo electrónico: ")

            guardar_estudiantes(estudiantes)
            print("Información actualizada correctamente.")
            return

    print("No se encontró un estudiante con esa matrícula.")
def eliminar_estudiante(estudiantes: list[dict[str, Any]]) -> None:
    """Elimina un estudiante utilizando su matrícula."""
    matricula = pedir_texto("Ingrese la matrícula del estudiante a eliminar: ")

    estudiante = encontrar_estudiante_por_matricula(estudiantes, matricula)

    if estudiante is None:
        print("No se encontró un estudiante con esa matrícula.")
        return

    print(f"Estudiante encontrado: {estudiante['nombre']}")

    confirmacion = input(
        "¿Desea eliminar este estudiante? (s/n): "
    ).strip().lower()

    if confirmacion == "s":
        estudiantes.remove(estudiante)
        guardar_estudiantes(estudiantes)
        print("Estudiante eliminado correctamente.")
    else:
        print("La eliminación fue cancelada.")

def mostrar_menu() -> None:
    """Muestra las opciones principales del programa."""
    print("1. Registrar estudiante")
print("2. Listar estudiantes")
print("3. Buscar estudiante")
print("4. Editar estudiante")
print("5. Eliminar estudiante")
print("6. Salir")

def main() -> None:
    """Ejecuta el menú principal hasta que el usuario decida salir."""
    estudiantes = cargar_estudiantes()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_estudiante(estudiantes)
        elif opcion == "2":
            listar_estudiantes(estudiantes)
        elif opcion == "3":
            buscar_estudiante(estudiantes)
        elif opcion == "4":
         editar_estudiante(estudiantes)
        elif opcion == "5":
         eliminar_estudiante(estudiantes)
        elif opcion == "6":
         print("Programa finalizado.")
        break


if __name__ == "__main__":
    main()
