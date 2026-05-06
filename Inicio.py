"""
☁️ WordCloud Studio — Nube de Palabras Profesional
"""

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re
import io
from collections import Counter
from wordcloud import WordCloud, STOPWORDS

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="WordCloud Studio",
    page_icon="☁️",
    layout="wide",
)

# ─────────────────────────────────────────────
# NUEVOS ESTILOS
# ─────────────────────────────────────────────
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Fondo */
.stApp {
    background-color: #f8fafc;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #ffffff !important;
    border-right: 2px solid #dbeafe;
}

/* Títulos */
h1 {
    color: #2563eb !important;
    font-weight: 700 !important;
}

h2, h3 {
    color: #1e40af !important;
}

/* Texto */
p, li, label {
    color: #374151 !important;
}

/* Header */
.header-card {
    background: white;
    padding: 30px;
    border-radius: 18px;
    border-left: 8px solid #2563eb;
    box-shadow: 0 4px 15px rgba(0,0,0,0.06);
    margin-bottom: 25px;
}

/* Cards */
.section-card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 4px 14px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}

/* Inputs */
textarea, input[type="text"] {
    border-radius: 12px !important;
    border: 2px solid #bfdbfe !important;
}

textarea:focus, input[type="text"]:focus {
    border-color: #2563eb !important;
    box-shadow: 0 0 0 3px rgba(37,99,235,0.15) !important;
}

/* Selectbox */
[data-baseweb="select"] > div {
    border-radius: 12px !important;
    border: 2px solid #bfdbfe !important;
}

/* Botones */
.stButton > button {
    background: linear-gradient(90deg, #2563eb, #60a5fa) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.03);
    box-shadow: 0 6px 18px rgba(37,99,235,0.25);
}

/* Download button */
[data-testid="stDownloadButton"] button {
    background: #111827 !important;
    color: white !important;
    border-radius: 12px !important;
}

/* Metrics */
[data-testid="metric-container"] {
    background: white;
    border-radius: 14px;
    border-top: 5px solid #2563eb;
    padding: 18px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.05);
}

/* Expander */
div[data-testid="stExpander"] {
    border-radius: 14px !important;
    border: 1px solid #dbeafe !important;
}

/* Wordcloud */
.wc-container {
    background: white;
    border-radius: 18px;
    padding: 20px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 4px 14px rgba(0,0,0,0.05);
}

/* Tags */
.uso-tag {
    background: #dbeafe;
    color: #1e3a8a;
    padding: 6px 14px;
    border-radius: 30px;
    display: inline-block;
    margin: 4px;
    font-size: 0.85rem;
    font-weight: 500;
}

</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────
st.markdown("""
<div class="header-card">
    <h1>☁️ WordCloud Studio</h1>
    <p>
        Genera nubes de palabras profesionales para visualizar los términos más frecuentes de un texto.
    </p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:

    st.markdown("## ⚙️ Configuración")

    texto_input = st.text_area(
        "✍️ Ingresa tu texto:",
        height=220,
        placeholder="Escribe o pega aquí un texto..."
    )

    st.markdown("---")

    paleta = st.selectbox(
        "🎨 Paleta de colores",
        ["Azul", "Verde", "Terracota", "Grises"]
    )

    max_words = st.slider(
        "🔠 Máximo de palabras",
        20, 200, 80
    )

    generar = st.button("☁️ Generar nube")

# ─────────────────────────────────────────────
# FUNCIONES
# ─────────────────────────────────────────────
def limpiar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r"[^a-záéíóúüñ\s]", " ", texto)
    return texto

def contar_palabras(texto):
    return Counter(texto.split())

PALETAS = {
    "Azul": ["#2563eb", "#60a5fa", "#1e40af"],
    "Verde": ["#059669", "#10b981", "#047857"],
    "Terracota": ["#c2410c", "#ea580c", "#fb923c"],
    "Grises": ["#111827", "#374151", "#9ca3af"]
}

def generar_wordcloud(texto, colores, max_words):

    import random

    def color_func(*args, **kwargs):
        return random.choice(colores)

    wc = WordCloud(
        width=1000,
        height=500,
        background_color="white",
        stopwords=set(STOPWORDS),
        max_words=max_words,
        color_func=color_func
    ).generate(texto)

    fig, ax = plt.subplots(figsize=(12,6))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")

    return fig

# ─────────────────────────────────────────────
# GENERAR
# ─────────────────────────────────────────────
if generar and texto_input.strip():

    texto_limpio = limpiar_texto(texto_input)

    frecuencias = contar_palabras(texto_limpio)

    # MÉTRICAS
    c1, c2, c3 = st.columns(3)

    c1.metric("Palabras", len(texto_limpio.split()))
    c2.metric("Vocabulario", len(frecuencias))
    c3.metric("Más frecuente", frecuencias.most_common(1)[0][0])

    st.markdown("<br>", unsafe_allow_html=True)

    # NUBE
    fig = generar_wordcloud(
        texto_limpio,
        PALETAS[paleta],
        max_words
    )

    st.markdown('<div class="wc-container">', unsafe_allow_html=True)

    st.pyplot(fig, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # TABLA
    st.markdown("### 📊 Frecuencia de palabras")

    df = pd.DataFrame(
        frecuencias.items(),
        columns=["Palabra", "Frecuencia"]
    ).sort_values(
        "Frecuencia",
        ascending=False
    )

    st.dataframe(df.head(20), use_container_width=True)

else:

    st.markdown("""
    <div class="section-card">
        <h3>📌 ¿Qué hace esta herramienta?</h3>

        <p>
        Esta aplicación genera una nube de palabras a partir de cualquier texto,
        resaltando visualmente las palabras más frecuentes.
        </p>

        <br>

        <span class="uso-tag">📚 Educación</span>
        <span class="uso-tag">📊 Análisis</span>
        <span class="uso-tag">📰 Noticias</span>
        <span class="uso-tag">💬 Comentarios</span>
        <span class="uso-tag">🤖 IA</span>

    </div>
    """, unsafe_allow_html=True)
