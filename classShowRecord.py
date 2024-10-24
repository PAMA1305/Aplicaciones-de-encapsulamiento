import tkinter as tk

class ShowRecord(tk.Tk):
    def __init__(self, api):
        super().__init__()
        self.api = api
        self.title("Último Registro de Estudiante")
        self.geometry("300x250")

        # Etiqueta para mostrar el registro
        self.etiqueta = tk.Label(self, text="", padx=10, pady=10)
        self.etiqueta.pack()

        # Botón para cargar el último registro
        boton = tk.Button(self, text="Mostrar Último Registro", command=self.mostrar_registro)
        boton.pack(pady=10)

    def mostrar_registro(self):
        registro = self.api.obtener_ultimo_registro()
        if registro:
            texto = (
                f"ID: {registro['id']}\n"
                f"Nombre: {registro['nombre']}\n"
                f"Apellido: {registro['apellido']}\n"
                f"Ciudad: {registro['ciudad']}\n"
                f"Calle: {registro['calle']}\n"
            )
            self.etiqueta.config(text=texto)
        else:
            self.etiqueta.config(text="No se pudo obtener el registro.")


