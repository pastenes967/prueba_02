import openai
import streamlit as st

# Configurar la clave API de OpenAI
openai.api_key = "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"

# Función para generar frases motivacionales
def generar_frase_motivacional():
    prompt = "Genera una frase motivacional corta y poderosa."
    
    # Llamada al modelo GPT-4-o-mini
    response = openai.Completion.create(
        engine="gpt-4o-mini",,  # Modelo específico
        prompt=prompt,
        max_tokens=60,          # Límite de palabras para la respuesta
        n=1,                    # Generar una sola frase
        stop=None,
        temperature=0.7         # Controla la creatividad
    )
    
    frase = response.choices[0].text.strip()
    return frase

# Interfaz de Streamlit
st.title("Generador de Frases Motivacionales")
st.write("Haz clic en el botón para recibir una frase motivacional.")

# Botón para generar frase
if st.button("Generar Frase"):
    frase = generar_frase_motivacional()
    st.write(f"💡 **Frase motivacional:** {frase}")
