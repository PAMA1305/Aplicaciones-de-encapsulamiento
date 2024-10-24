import requests

class GetRecord:
    def __init__(self):
        self.url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"

    def obtener_ultimo_registro(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            estudiantes = response.json()
            if estudiantes:
                return estudiantes[-1]  # Obtiene el último registro
        return None



