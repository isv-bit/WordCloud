"""
☁️ WordCloud Studio — Nube de Palabras
"""

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import re
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
# ESTILOS
# ─────────────────────────────────────────────
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* FUENTE */
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* FONDO GENERAL */
.stApp {
    background-color: #0f172a !important;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background-color: #111827 !important;
    border-right: 2px solid #2563eb;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

/* TITULOS */
h1 {
    color: #60a5fa !important;
    font-weight: 700 !important;
}

h2, h3 {
    color: #93c5fd !important;
}

/* TEXTO */
p, label, span {
    color: #f3f4f6 !important;
}

/* HEADER */
.header-card {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    padding: 35px;
    border-radius: 22px;
    margin-bottom: 30px;
    box-shadow: 0 8px 25px rgba(37,99,235,0.35);
}

/* CARDS */
.section-card {
    background: #111827;
    border: 2px solid #2563eb;
    padding: 25px;
    border-radius: 20px;
    margin-bottom: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.35);
}

/* INPUTS */
textarea, input[type="text"] {
    background-color: #1e293b !important;
    color: white !important;
    border: 2px solid #3b82f6 !important;
    border-radius: 14px !important;
}

/* SELECT */
[data-baseweb="select"] > div {
    background-color: #1e293b !important;
    border: 2px solid #3b82f6 !important;
    border-radius: 14px !important;
    color: white !important;
}

/* BOTONES */
.stButton > button {
    background: linear-gradient(90deg, #2563eb, #60a5fa) !important;
    color: white !important;
    border: none !important;
    border-radius: 14px !important;
    font-weight: 700 !important;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.03);
    box-shadow: 0 8px 20px rgba(37,99,235,0.35);
}

/* MÉTRICAS */
[data-testid="metric-container"] {
    background: #111827;
    border: 2px solid #2563eb;
    border-radius: 16px;
    padding: 18px;
}

[data-testid="metric-container"] * {
    color: white !important;
}

/* TABLAS */
[data-testid="stDataFrame"] {
    background-color: #111827 !important;
    border-radius: 16px;
    overflow: hidden;
}

/* CONTENEDOR NUBE */
.wc-container {
    background: #111827;
    border: 2px solid #2563eb;
    border-radius: 20px;
    padding: 20px;
}

/* TAGS */
.uso-tag {
    background: #2563eb;
    color: white !important;
    padding: 7px 16px;
    border-radius: 30px;
    display: inline-block;
    margin: 5px;
    font-size: 0.85rem;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────
st.markdown("""
<div class="header-card">

    <h1 style="color:white;">
        ☁️ WordCloud Studio
    </h1>

    <p style="color:white; font-size:18px;">
        Genera nubes de palabras visuales a partir de cualquier texto.
    </p>

</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:

    st.title("⚙️ Configuración")

    texto_input = st.text_area(
        "✍️ Ingresa un texto",
        height=220,
        placeholder="Escribe o pega aquí tu texto..."
    )

    paleta = st.selectbox(
        "🎨 Paleta",
        ["Azul", "Verde", "Terracota", "Morado"]
    )

    max_words = st.slider(
        "🔠 Máximo de palabras",
        20,
        200,
        80
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
    "Azul": ["#2563eb", "#60a5fa", "#93c5fd"],
    "Verde": ["#059669", "#10b981", "#6ee7b7"],
    "Terracota": ["#c2410c", "#ea580c", "#fdba74"],
    "Morado": ["#7c3aed", "#8b5cf6", "#c4b5fd"]
}


def generar_wordcloud(texto, colores, max_words):

    import random

    def color_func(*args, **kwargs):
        return random.choice(colores)

    wc = WordCloud(
        width=1000,
        height=500,
        background_color="#111827",
        stopwords=set(STOPWORDS),
        max_words=max_words,
        color_func=color_func,
        collocations=False
    ).generate(texto)

    fig, ax = plt.subplots(figsize=(12,6))
    fig.patch.set_facecolor("#111827")

    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")

    return fig


# ─────────────────────────────────────────────
# APP
# ─────────────────────────────────────────────
if generar and texto_input.strip():

    texto_limpio = limpiar_texto(texto_input)

    frecuencias = contar_palabras(texto_limpio)

    # MÉTRICAS
    c1, c2, c3 = st.columns(3)

    c1.metric("Palabras", len(texto_limpio.split()))
    c2.metric("Vocabulario", len(frecuencias))
    c3.metric(
        "Más frecuente",
        frecuencias.most_common(1)[0][0]
    )

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

    st.markdown("### 📊 Frecuencia de palabras")

    df = pd.DataFrame(
        frecuencias.items(),
        columns=["Palabra", "Frecuencia"]
    ).sort_values(
        "Frecuencia",
        ascending=False
    )

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

else:

    st.markdown("""
    <div class="section-card">

        <h2>📌 ¿Qué hace esta herramienta?</h2>

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
