st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* FUENTE */
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* FONDO GENERAL NEGRO */
.stApp {
    background-color: #0f172a !important;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background-color: #111827 !important;
    border-right: 2px solid #2563eb;
}

/* TEXOS SIDEBAR */
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
    padding: 30px;
    border-radius: 20px;
    margin-bottom: 25px;
    box-shadow: 0 8px 25px rgba(37,99,235,0.35);
}

/* CARDS */
.section-card {
    background: #111827;
    border: 2px solid #2563eb;
    padding: 25px;
    border-radius: 18px;
    margin-bottom: 20px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.35);
}

/* INPUTS */
textarea, input[type="text"] {
    background-color: #1e293b !important;
    color: white !important;
    border: 2px solid #3b82f6 !important;
    border-radius: 14px !important;
}

/* SELECTBOX */
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

/* METRICAS */
[data-testid="metric-container"] {
    background: #111827;
    border: 2px solid #2563eb;
    border-radius: 16px;
    padding: 18px;
}

/* TEXO METRICAS */
[data-testid="metric-container"] * {
    color: white !important;
}

/* TABLAS */
[data-testid="stDataFrame"] {
    background-color: #111827 !important;
    border-radius: 16px;
    overflow: hidden;
}

/* WORDCLOUD CARD */
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

/* EXPANDER */
.streamlit-expanderHeader {
    background-color: #111827 !important;
    color: white !important;
}

/* SCROLL */
::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-thumb {
    background: #2563eb;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)
