import gradio as gr
import requests

API_URL = "http://localhost:8000"  # Asume que FastAPI se ejecuta en localhost en el puerto 8000

def get_user_data_from_api(user):
    response = requests.get(f"{API_URL}/user_data/{user}")
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"

def launch_interface():
    # Obtiene la lista de usuarios desde la API
    users_response = requests.get(f"{API_URL}/users/")
    if users_response.status_code != 200:
        print("Error al obtener la lista de usuarios.")
        return

    users = users_response.json()

    iface = gr.Interface(
        fn=get_user_data_from_api,
        inputs=gr.Dropdown(choices=users),
        outputs=gr.Dataframe(),
        title="Consulta de Datos de Usuarios"
    )
    iface.launch()

if __name__ == "__main__":
    launch_interface()
