"""
Sistema básico para registrar y consultar estudiantes.

El programa permite:
- Registrar estudiantes.
- Listar estudiantes.
- Buscar estudiantes.
- Editar estudiantes.
- Eliminar estudiantes.
- Mostrar estadísticas.
- Guardar la información en un archivo JSON.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


# ============================================================
# CONFIGURACIÓN DEL ARCHIVO
# ============================================================

DATA_FILE = Path(__file__).parent / "data" / "estudiantes.json"


# ============================================================
# CARGAR Y GUARDAR ESTUDIANTES
# ============================================================

def cargar_estudiantes() -> list[dict[str, Any]]:
    """Devuelve los estudiantes guardados o una lista vacía."""

    if not DATA_FILE.exists():
        return []

    try:
        contenido = DATA_FILE.read_text(encoding="utf-8")
        datos = json.loads(contenido)

        if isinstance(datos, list):
            return datos

        print("El archivo de datos no tiene un formato válido.")
        return []

    except (OSError, json.JSONDecodeError):
        print(
            "No se pudo leer el archivo de datos. "
            "Se continuará con una lista vacía."
        )
        return []


def guardar_estudiantes(
    estudiantes: list[dict[str, Any]]
) -> None:
    """Guarda la lista de estudiantes en formato JSON."""

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    DATA_FILE.write_text(
        json.dumps(
            estudiantes,
            ensure_ascii=False,
            indent=4
        ),
        encoding="utf-8"
    )


# ============================================================
# VALIDACIONES
# ============================================================

def pedir_texto(mensaje: str) -> str:
    """Solicita un texto y evita que se guarde vacío."""

    while True:

        valor = input(mensaje).strip()

        if valor:
            return valor

        print("ERROR: El dato no puede quedar vacío.")


def pedir_nombre(mensaje: str) -> str:
    """Solicita un nombre válido."""

    while True:

        nombre = input(mensaje).strip()

        if not nombre:
            print("ERROR: El nombre no puede quedar vacío.")
            continue

        if any(caracter.isdigit() for caracter in nombre):
            print("ERROR: El nombre no puede contener números.")
            continue

        return nombre


def pedir_matricula(mensaje: str) -> str:
    """Solicita una matrícula formada únicamente por números."""

    while True:

        matricula = input(mensaje).strip()

        if not matricula:
            print("ERROR: La matrícula no puede quedar vacía.")
            continue

        if not matricula.isdigit():
            print(
                "ERROR: La matrícula debe contener "
                "únicamente números."
            )
            continue

        return matricula


def pedir_correo(mensaje: str) -> str:
    """Solicita un correo electrónico con un formato básico válido."""

    while True:

        correo = input(mensaje).strip()

        if not correo:
            print("ERROR: El correo no puede quedar vacío.")
            continue

        if "@" not in correo or "." not in correo.split("@")[-1]:
            print("ERROR: Ingrese un correo electrónico válido.")
            continue

        return correo


def pedir_confirmacion(mensaje: str) -> bool:
    """Solicita una confirmación de tipo sí/no."""

    while True:

        respuesta = input(mensaje).strip().lower()

        if respuesta in ("s", "si", "sí"):
            return True

        if respuesta in ("n", "no"):
            return False

        print("ERROR: Responda utilizando 's' o 'n'.")


# ============================================================
# BÚSQUEDA
# ============================================================

def encontrar_estudiante_por_matricula(
    estudiantes: list[dict[str, Any]],
    matricula: str
) -> dict[str, Any] | None:
    """Busca un estudiante por su matrícula."""

    for estudiante in estudiantes:

        if estudiante["matricula"] == matricula:
            return estudiante

    return None


def buscar_estudiante(
    estudiantes: list[dict[str, Any]]
) -> None:
    """Permite buscar un estudiante por matrícula o nombre."""

    if not estudiantes:
        print("\nNo existen estudiantes registrados.")
        return

    print("\n========================================")
    print("          BUSCAR ESTUDIANTE")
    print("========================================")
    print("1. Buscar por matrícula")
    print("2. Buscar por nombre")
    print("3. Volver")
    print("========================================")

    while True:

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":

            matricula = pedir_matricula(
                "Ingrese la matrícula: "
            )

            estudiante = encontrar_estudiante_por_matricula(
                estudiantes,
                matricula
            )

            if estudiante is None:

                print(
                    "No se encontró un estudiante "
                    "con esa matrícula."
                )

            else:

                mostrar_datos_estudiante(estudiante)

            return

        elif opcion == "2":

            nombre = pedir_texto(
                "Ingrese el nombre a buscar: "
            ).lower()

            encontrados = []

            for estudiante in estudiantes:

                if nombre in estudiante["nombre"].lower():
                    encontrados.append(estudiante)

            if not encontrados:

                print(
                    "No se encontraron estudiantes "
                    "con ese nombre."
                )

            else:

                print(
                    f"\nSe encontraron "
                    f"{len(encontrados)} estudiante(s):"
                )

                for estudiante in encontrados:
                    mostrar_datos_estudiante(estudiante)

            return

        elif opcion == "3":

            return

        else:

            print(
                "ERROR: Seleccione una opción entre 1 y 3."
            )


# ============================================================
# MOSTRAR INFORMACIÓN
# ============================================================

def mostrar_datos_estudiante(
    estudiante: dict[str, Any]
) -> None:
    """Muestra la información de un estudiante."""

    print("\n----------------------------------------")
    print(f"Matrícula: {estudiante['matricula']}")
    print(f"Nombre:    {estudiante['nombre']}")
    print(f"Carrera:   {estudiante['carrera']}")
    print(f"Correo:    {estudiante['correo']}")
    print("----------------------------------------")


def listar_estudiantes(
    estudiantes: list[dict[str, Any]]
) -> None:
    """Muestra todos los estudiantes registrados."""

    if not estudiantes:

        print("\nTodavía no existen estudiantes registrados.")
        return

    print("\n========================================")
    print("        ESTUDIANTES REGISTRADOS")
    print("========================================")

    for numero, estudiante in enumerate(
        estudiantes,
        start=1
    ):

        print(f"\nEstudiante #{numero}")

        mostrar_datos_estudiante(estudiante)


# ============================================================
# REGISTRAR ESTUDIANTE
# ============================================================

def registrar_estudiante(
    estudiantes: list[dict[str, Any]]
) -> None:
    """Registra un estudiante si la matrícula no existe."""

    print("\n========================================")
    print("         REGISTRAR ESTUDIANTE")
    print("========================================")

    matricula = pedir_matricula("Matrícula: ")

    # Verificar matrícula duplicada
    if encontrar_estudiante_por_matricula(
        estudiantes,
        matricula
    ) is not None:

        print(
            "ERROR: Ya existe un estudiante "
            "con esa matrícula."
        )
        return

    nombre = pedir_nombre(
        "Nombre completo: "
    )

    carrera = pedir_texto(
        "Carrera: "
    )

    correo = pedir_correo(
        "Correo electrónico: "
    )

    nuevo_estudiante = {
        "matricula": matricula,
        "nombre": nombre,
        "carrera": carrera,
        "correo": correo,
    }

    estudiantes.append(nuevo_estudiante)

    guardar_estudiantes(estudiantes)

    print("\n========================================")
    print("Estudiante registrado correctamente.")
    print("========================================")


# ============================================================
# EDITAR ESTUDIANTE
# ============================================================

def editar_estudiante(
    estudiantes: list[dict[str, Any]]
) -> None:
    """Permite modificar la información de un estudiante."""

    if not estudiantes:

        print("\nNo existen estudiantes registrados.")
        return

    print("\n========================================")
    print("          EDITAR ESTUDIANTE")
    print("========================================")

    matricula = pedir_matricula(
        "Ingrese la matrícula del estudiante: "
    )

    estudiante = encontrar_estudiante_por_matricula(
        estudiantes,
        matricula
    )

    if estudiante is None:

        print(
            "No se encontró un estudiante "
            "con esa matrícula."
        )
        return

    print("\nEstudiante encontrado:")
    mostrar_datos_estudiante(estudiante)

    if not pedir_confirmacion(
        "\n¿Desea editar este estudiante? (s/n): "
    ):
        print("La edición fue cancelada.")
        return

    # Nueva matrícula
    while True:

        nueva_matricula = pedir_matricula(
            "Nueva matrícula: "
        )

        # Si mantiene la misma matrícula
        if nueva_matricula == estudiante["matricula"]:
            break

        # Comprobar si la nueva matrícula ya existe
        otro_estudiante = encontrar_estudiante_por_matricula(
            estudiantes,
            nueva_matricula
        )

        if otro_estudiante is not None:

            print(
                "ERROR: Esa matrícula ya pertenece "
                "a otro estudiante."
            )

        else:
            break

    estudiante["matricula"] = nueva_matricula

    estudiante["nombre"] = pedir_nombre(
        "Nuevo nombre completo: "
    )

    estudiante["carrera"] = pedir_texto(
        "Nueva carrera: "
    )

    estudiante["correo"] = pedir_correo(
        "Nuevo correo electrónico: "
    )

    guardar_estudiantes(estudiantes)

    print(
        "\nInformación actualizada correctamente."
    )


# ============================================================
# ELIMINAR ESTUDIANTE
# ============================================================

def eliminar_estudiante(
    estudiantes: list[dict[str, Any]]
) -> None:
    """Elimina un estudiante utilizando su matrícula."""

    if not estudiantes:

        print("\nNo existen estudiantes registrados.")
        return

    print("\n========================================")
    print("         ELIMINAR ESTUDIANTE")
    print("========================================")

    matricula = pedir_matricula(
        "Ingrese la matrícula del estudiante: "
    )

    estudiante = encontrar_estudiante_por_matricula(
        estudiantes,
        matricula
    )

    if estudiante is None:

        print(
            "No se encontró un estudiante "
            "con esa matrícula."
        )
        return

    print("\nEstudiante encontrado:")
    mostrar_datos_estudiante(estudiante)

    confirmacion = pedir_confirmacion(
        "\n¿Desea eliminar este estudiante? (s/n): "
    )

    if confirmacion:

        estudiantes.remove(estudiante)

        guardar_estudiantes(estudiantes)

        print(
            "Estudiante eliminado correctamente."
        )

    else:

        print("La eliminación fue cancelada.")


# ============================================================
# ESTADÍSTICAS
# ============================================================

def mostrar_estadisticas(
    estudiantes: list[dict[str, Any]]
) -> None:
    """Muestra un resumen de los estudiantes registrados."""

    if not estudiantes:

        print("\nNo existen estudiantes registrados.")
        return

    carreras: dict[str, int] = {}

    for estudiante in estudiantes:

        carrera = estudiante["carrera"]

        if carrera in carreras:
            carreras[carrera] += 1
        else:
            carreras[carrera] = 1

    print("\n========================================")
    print("       ESTADÍSTICAS DE ESTUDIANTES")
    print("========================================")

    print(
        f"Total de estudiantes: {len(estudiantes)}"
    )

    print("\nEstudiantes por carrera:")

    for carrera, cantidad in carreras.items():

        print(
            f"- {carrera}: {cantidad}"
        )


# ============================================================
# MENÚ
# ============================================================

def mostrar_menu() -> None:
    """Muestra las opciones principales."""

    print("\n========================================")
    print("       SISTEMA DE ESTUDIANTES")
    print("========================================")
    print("1. Registrar estudiante")
    print("2. Listar estudiantes")
    print("3. Buscar estudiante")
    print("4. Editar estudiante")
    print("5. Eliminar estudiante")
    print("6. Ver estadísticas")
    print("7. Salir")
    print("========================================")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main() -> None:
    """Ejecuta el menú principal."""

    estudiantes = cargar_estudiantes()

    while True:

        mostrar_menu()

        opcion = input(
            "Seleccione una opción: "
        ).strip()

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

            mostrar_estadisticas(estudiantes)

        elif opcion == "7":

            print("\nPrograma finalizado.")
            break

        else:

            print(
                "\nERROR: Opción no válida."
            )
            print(
                "Seleccione una opción entre 1 y 7."
            )


# ============================================================
# INICIO DEL PROGRAMA
# ============================================================

if __name__ == "__main__":
    main()