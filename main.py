from fastapi import FastAPI
from typing import List
import pandas as pd
import gradio as gr
import requests
from fastapi.responses import HTMLResponse


app = FastAPI()

# Carga de datos desde el archivo Excel
df = pd.read_excel('Staff Feedback - PX _ Specialists _ RRHH.xlsx')

@app.get("/users/", response_model=List[str])
async def get_users():
    return df['User'].unique().tolist()

@app.get("/user_data/{user}", response_class=HTMLResponse)
async def get_user_data(user: str):
    try:
        user_data = df[df['User'] == user].sort_values(by='Fecha entrevista', ascending=False).head(5)

        entrevistas_html = "<div>"
        for _, row in user_data.iterrows():
            fecha = row['Fecha entrevista'].strftime("%Y-%m-%d") if pd.notnull(row['Fecha entrevista']) else "Fecha no disponible"
            happiness = f"Felicidad: {row['Happiness']}" if pd.notnull(row['Happiness']) else "Felicidad no disponible"
            enviado_por = f"Entrevistado por: {row['Enviado por']}" if pd.notnull(row['Enviado por']) else "Entrevistador no disponible"
            comentarios = row['Comentarios Generales'] if pd.notnull(row['Comentarios Generales']) else "Sin comentarios"
            entrevista = f"<p><strong>Fecha:</strong> {fecha}<br><strong>{happiness}</strong><br>{enviado_por}<br>{comentarios}</p><hr>"
            entrevistas_html += entrevista
        entrevistas_html += "</div>"

        return entrevistas_html
    except KeyError as e:
        return f"Error: La columna no existe - {e}"



# Define la función para la interfaz de Gradio
def get_user_data_from_api(user):
    response = requests.get(f"http://localhost:8000/user_data/{user}")
    if response.status_code == 200:
        return response.text  # Obtener el texto de la respuesta
    else:
        return f"Error: {response.status_code}"

# Crea la interfaz de Gradio
io = gr.Interface(
    fn=get_user_data_from_api,
    inputs=gr.Dropdown(choices=df['User'].unique().tolist()),
    outputs=gr.HTML(),  # Cambiar la salida a HTML para renderizar correctamente
    title="Consulta de Datos de Usuarios"
)

# Monta la interfaz de Gradio en la aplicación FastAPI
app = gr.mount_gradio_app(app, io, path="/gradio")
