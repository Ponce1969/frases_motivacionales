import streamlit as st # se instala con pip install streamlit
import requests # se instala con pip install requests
from translate import Translator # se instala con pip install translate, con googletrans no funciona.

# Título de la página
st.title("Frase motivacional")

def obtener_frase():
    """
    Obtiene una frase motivacional de la API.

    Returns:
        str: La frase motivacional traducida.
    """
    try:
        url = "https://api.quotable.io/random"
        response = requests.get(url)
        if response.status_code == 200:
            frase = response.json()["content"]
            frase = traducir_texto(frase)
            autor = response.json()["author"]
            return [frase , autor] # Devuelve la frase y el autor
        else:
            st.error("Error, no se ha podido conectar con la API")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Error, no se ha podido conectar con la API: {str(e)}")
        return None

def traducir_texto(texto):
    """
    Traduce un texto de inglés a español.

    Args:
        texto (str): El texto a traducir.

    Returns:
        str: El texto traducido.
    """
    try:
        translator = Translator(from_lang="en", to_lang="es", provision_dict={"quality": "fast"})
        frase_traducida = translator.translate(texto)
        return frase_traducida
    except Exception as e:
        st.error(f"Error, no se ha podido traducir el texto: {str(e)}")
        return None

def exibir_frase():
    """
    Muestra una frase motivacional en un papiro estilizado.
    """
    frase_motivacional = obtener_frase()

    # Formato del papiro
    papiro_style = """
        <style>
            .papiro {
                display: flex;
                flex-direction: column;
                background-color:#365233;
                padding: 70px;
                border-radius:20px;
                font-family: 'Book Antiqua', 'Times New Roman', Palatino, serif;
                font-size:34px;    /* Tamaño de la letra */
                color: white;      /* Color del texto */
            }
            .papiro em {
                align-self: flex-end;
                padding-top: 20px;
                }
                
        </style>
    """

    # Mostrar la frase dentro del papiro
    st.markdown(papiro_style, unsafe_allow_html=True)
    st.markdown(f'<div class="papiro">{frase_motivacional[0]}<br><em>{frase_motivacional[1]}</em></div>', unsafe_allow_html=True)

# Llamar a la función
exibir_frase()

