import tkinter as tk
import requests


def obtener_ultimo_registro():
    url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"
    response = requests.get(url)
    if response.status_code == 200:
        estudiantes = response.json()
        if estudiantes:
            return estudiantes[-1]  # Obtiene el último registro
    return None

def mostrar_registro():
    registro = obtener_ultimo_registro()
    if registro:
        texto = (
            f"ID: {registro['id']}\n"
            f"Nombre: {registro['nombre']}\n"
            f"Apellido: {registro['apellido']}\n"
            f"Ciudad: {registro['ciudad']}\n"
            f"Calle: {registro['calle']}\n"
        )
        etiqueta.config(text=texto)
    else:
        etiqueta.config(text="No se pudo obtener el registro.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Último Registro de Estudiante")
ventana.geometry("300x250")

# Etiqueta para mostrar el registro
etiqueta = tk.Label(ventana, text="", padx=10, pady=10)
etiqueta.pack()

# Botón para cargar el último registro
boton = tk.Button(ventana, text="Mostrar Último Registro", command=mostrar_registro)
boton.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
