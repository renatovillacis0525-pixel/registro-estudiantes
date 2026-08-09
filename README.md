# Registro de estudiantes

## Descripción

Este proyecto consiste en una aplicación básica desarrollada en Python para registrar y consultar información de estudiantes.

El programa fue creado inicialmente para practicar el uso de Git y GitHub, pero durante las diferentes actividades se fueron agregando nuevas funcionalidades. Actualmente permite registrar estudiantes, buscarlos, modificar sus datos, eliminarlos y consultar un pequeño resumen de la información almacenada.

Los datos se guardan localmente en un archivo JSON generado durante la ejecución del programa.

## Objetivo

Desarrollar una aplicación sencilla que permita administrar información básica de estudiantes y, al mismo tiempo, aplicar buenas prácticas de desarrollo como el control de versiones con Git, el uso de GitHub, la organización del código y la documentación del repositorio.

## Funcionalidades

El programa cuenta con las siguientes opciones:

- Registrar nuevos estudiantes.
- Evitar matrículas duplicadas.
- Validar que la matrícula contenga únicamente números.
- Listar los estudiantes registrados.
- Buscar estudiantes por matrícula o nombre.
- Editar la información de un estudiante.
- Eliminar estudiantes mediante su matrícula.
- Confirmar antes de eliminar un registro.
- Consultar el total de estudiantes registrados.
- Mostrar la cantidad de estudiantes por carrera.
- Guardar la información en formato JSON.

## Tecnologías utilizadas

- Python 3.
- Visual Studio Code.
- Git.
- GitHub.
- JSON para el almacenamiento local de los datos.

## Estructura del proyecto

```text
registro-estudiantes/
│
├── data/
│   └── estudiantes.json
│
├── .gitignore
├── main.py
└── README.md