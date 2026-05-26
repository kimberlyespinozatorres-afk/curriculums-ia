import streamlit as st

st.set_page_config(
    page_title="Usar con Gemini - ORH UCR",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .main-title { font-size: 32px; font-weight: bold; color: #042d62; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size: 18px; color: #0076a8; text-align: center; margin-bottom: 30px; font-weight: bold;}
    .section-header { font-size: 22px; font-weight: bold; color: #042d62; border-bottom: 2px solid #0076a8; padding-bottom: 5px; margin-top: 20px; margin-bottom: 15px; }
    .info-box { background-color: #f0f4f8; padding: 15px; border-radius: 8px; border-left: 5px solid #0076a8; margin-bottom: 20px; border-top: 1px solid #0076a8; border-right: 1px solid #0076a8; border-bottom: 1px solid #0076a8;}
    .step-box { background-color: #eaf4fb; padding: 12px 18px; border-radius: 8px; margin-bottom: 10px; border-left: 4px solid #0076a8; font-size: 15px;}
    .stButton>button { background-color: #0076a8; color: white; border-radius: 5px; border: none; font-size: 15px;}
    .stButton>button:hover { background-color: #042d62; color: white;}
    .identidad-encabezado { text-align: center; margin-bottom: 20px;}
    </style>
""", unsafe_allow_html=True)

# Encabezado UCR
st.markdown("""
<div class="identidad-encabezado">
    <img src="https://ucr.ac.cr/medios/imagenes/2015/firma-ucr-institucional-azul.png" width="280px" alt="UCR logo">
    <div style="color: #042d62; font-size: 22px; font-weight: bold; margin-top: 10px;">Oficina de Recursos Humanos (ORH)</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Evaluación Manual con Gemini</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Alternativa sin costo — Copie el prompt y úselo directamente en Gemini</div>', unsafe_allow_html=True)

# ── Pasos ──────────────────────────────────────────────────────────────────────
st.markdown('<div class="section-header">📋 ¿Cómo proceder?</div>', unsafe_allow_html=True)

st.markdown('<div class="step-box">1️⃣ &nbsp; Copie el prompt de la sección inferior con el botón <strong>"Copiar Prompt"</strong>.</div>', unsafe_allow_html=True)
st.markdown('<div class="step-box">2️⃣ &nbsp; Abra Gemini con el botón <strong>"Abrir Gemini"</strong> (use su cuenta institucional UCR).</div>', unsafe_allow_html=True)
st.markdown('<div class="step-box">3️⃣ &nbsp; Pegue el prompt en el chat de Gemini (<strong>Ctrl+V</strong> o <strong>Cmd+V</strong>).</div>', unsafe_allow_html=True)
st.markdown('<div class="step-box">4️⃣ &nbsp; Adjunte el <strong>PDF del Perfil del Puesto</strong> y el <strong>PDF del CV</strong> directamente en Gemini.</div>', unsafe_allow_html=True)
st.markdown('<div class="step-box">5️⃣ &nbsp; Presione Enter y obtenga el reporte completo.</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Botón Gemini ───────────────────────────────────────────────────────────────
st.markdown('<div class="section-header">🤖 Acceder a Gemini</div>', unsafe_allow_html=True)
st.markdown("""
<div class="info-box">
    <strong>Gemini — Google</strong><br>
    Plataforma de inteligencia artificial de Google. Pegue el prompt y adjunte los documentos del proceso para obtener su reporte de evaluación de forma inmediata y sin costo.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<a href="https://gemini.google.com/app?hl=es" target="_blank">
    <button style="background-color:#0076a8; color:white; border:none; border-radius:8px;
                   padding:12px 28px; font-size:16px; cursor:pointer; font-weight:bold;">
        🚀 Abrir Gemini ahora
    </button>
</a>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Prompt ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="section-header">📄 Prompt para copiar</div>', unsafe_allow_html=True)

# Si viene de la app principal, usar el prompt guardado; si no, usar el prompt base
if "prompt_para_gemini" in st.session_state and st.session_state["prompt_para_gemini"]:
    prompt_mostrar = st.session_state["prompt_para_gemini"]
    st.info("✅ Prompt generado automáticamente desde los documentos cargados en la página principal.")
else:
    prompt_mostrar = """Actúa como un Consultor Experto en Reclutamiento y Selección de Personal de la Oficina de Recursos Humanos (ORH) de la Universidad de Costa Rica (UCR), especializado en la gestión de talento humano del sector público y universitario.

Tu objetivo es realizar un análisis técnico, objetivo y estandarizado para evaluar el nivel de ajuste de un candidato frente al perfil oficial de un puesto de trabajo.

Para ello, te proporcionaré dos insumos clave:
1. El Perfil del Cargo / Requisitos Oficiales (adjunto en este mensaje).
2. El Currículum Vitae (CV) del postulante (adjunto en este mensaje).

Por favor, genera un "Reporte de Evaluación y Ajuste de Candidatos" estructurado con las siguientes secciones:

### 1. RESUMEN EJECUTIVO DE LA CANDIDATURA
- Nombre del Candidato
- Puesto al que postula y Unidad de Destino
- Calificación Final (escala 1 al 10)
- Estatus Sugerido: [PASA A ENTREVISTA / ELEGIBLE EN RESERVA / NO PRESELECCIONADO]

### 2. MATRIZ DE CALIFICACIÓN DETALLADA (Tabla)
| Criterio de Evaluación | Requisito del Puesto | Perfil del Candidato | Nivel de Cumplimiento | Nota (1-10) y Justificación |

### 3. ANÁLISIS CUALITATIVO EN VIÑETAS
- Fortalezas Clave (puntos fuertes y valor agregado)
- Brechas / Puntos Ciegos (faltas en el perfil o aspectos a evaluar en entrevista)

### 4. RECOMENDACIÓN FINAL DE LA ORH
Dictamen técnico y objetivo sobre si el candidato debe avanzar a la siguiente fase del proceso, justificando la decisión de manera profesional conforme a la normativa UCR.

---
[Adjunte el Perfil del Puesto y el CV directamente en este chat de Gemini]"""
    st.warning("⚠️ Cargue primero los documentos en la página principal para obtener un prompt personalizado. Este es el prompt base estándar.")

# Caja copiable
st.code(prompt_mostrar, language="markdown")

# Botón descarga como respaldo
st.download_button(
    label="⬇️ Descargar Prompt como .txt",
    data=prompt_mostrar,
    file_name="prompt_AEP_ORH_Gemini.txt",
    mime="text/plain"
)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; color:#888; font-size:13px;">
    Este recurso es de apoyo técnico. La decisión final corresponde al profesional de Reclutamiento y Selección conforme a la normativa vigente de la UCR.
</div>
""", unsafe_allow_html=True)
