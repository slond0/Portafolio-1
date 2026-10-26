"""
PORTAFOLIO · SARA LONDOÑO  —  Streamlit
Ejecutar:  streamlit run app.py

Todo lo editable está en la sección "1. CONTENIDO EDITABLE".
Imágenes y videos: pon los archivos en la carpeta  assets/  y escribe la ruta
(ej. "assets/lovepaws_1.png") o pega un enlace https://...
Si un archivo no existe, se muestra un recuadro de reemplazo.
"""
import base64
from pathlib import Path
from urllib.parse import quote

import streamlit as st

st.set_page_config(page_title="Sara Londoño · Portafolio", page_icon="✦", layout="wide")

# ══════════════════════════════════════════════════════════════
# 1. CONTENIDO EDITABLE
# ══════════════════════════════════════════════════════════════
PERFIL = {
    "nombre": "Sara Londoño",
    "formacion": "Comunicación Social · Diseño Interactivo",
    "especialidades": "UX/UI · Comunicación digital · Diseño visual · Creación de contenido",
    "foto": "assets/sara.jpg",
    "hero_video": "assets/hero.mp4",          # video de fondo (corto, <15 MB)
    "descripcion": (
        "Soy comunicadora social y diseñadora interactiva. Investigo, conceptualizo, "
        "diseño y comunico soluciones creativas que conectan personas, tecnología y marcas. "
        "Me interesa el diseño centrado en las personas y las experiencias digitales con sentido."
    ),
    "email": "tucorreo@gmail.com",             # ← CAMBIA ESTO
    "telefono": "+57 300 000 0000",            # ← CAMBIA ESTO
    "whatsapp": "573000000000",                # solo números, con indicativo
    "linkedin": "https://www.linkedin.com/in/tu-perfil",
    "ubicacion": "Medellín, Colombia",
    "cv_pdf": "assets/CV_Sara_Londono.pdf",
}

HABILIDADES = {
    "UX/UI y diseño de experiencias": [
        "Diseño centrado en las personas", "Investigación de usuarios",
        "Arquitectura de información", "Diseño de interfaces", "Prototipado",
        "Diseño visual de productos digitales"],
    "Comunicación y marketing": [
        "Estrategia de comunicación", "Comunicación digital", "Copywriting",
        "Creación de contenido", "Planeación de contenidos", "Relaciones públicas"],
    "Diseño visual y experiencias interactivas": [
        "Diseño gráfico", "Identidad visual", "Edición audiovisual",
        "Modelado 3D", "Experiencias interactivas"],
    "Herramientas y tecnologías": [
        "Figma", "Photoshop", "Illustrator", "Premiere Pro", "CapCut",
        "Maya", "Unity", "HTML", "CSS", "Excel"],
}

HOJA_DE_VIDA = {
    "perfil": "Resumen profesional: escribe aquí 3–4 líneas sobre tu perfil.",
    "experiencia": [
        ("2025 – Actualidad", "Cargo / Proyecto", "Organización",
         "Responsabilidades y logros principales."),
        ("2024 – 2025", "Cargo / Proyecto", "Organización",
         "Responsabilidades y logros principales."),
    ],
    "formacion": [
        ("Universidad", "Comunicación Social", "Años"),
        ("Universidad", "Diseño Interactivo", "Años"),
    ],
    "cursos": ["Curso o diplomado 1", "Curso o diplomado 2"],
    "idiomas": [("Español", "Nativo"), ("Inglés", "Nivel (B2, C1...)")],
}

CATEGORIAS = [
    {
        "id": "3d", "nombre": "Experiencias inmersivas y 3D", "icono": "🧊",
        "intro": "Modelado 3D, videojuegos, entornos virtuales y experiencias interactivas. "
                 "Aquí muestro mi capacidad de construir mundos, objetos y experiencias digitales.",
    },
    {
        "id": "ux", "nombre": "UX/UI y productos digitales", "icono": "📱",
        "intro": "Interfaces, prototipos, investigación de usuarios, arquitectura de información, "
                 "flujos y soluciones de diseño centradas en las personas.",
    },
    {
        "id": "visual", "nombre": "Diseño visual y dirección creativa", "icono": "🎨",
        "intro": "Identidad visual, piezas gráficas, campañas, composición, fotografía, "
                 "diseño editorial y exploración estética.",
    },
    {
        "id": "inv", "nombre": "Investigación y estrategia", "icono": "🔎",
        "intro": "Investigación de públicos, entrevistas, encuestas, análisis de percepciones, "
                 "hallazgos y propuestas estratégicas.",
    },
    {
        "id": "cont", "nombre": "Comunicación y creación de contenido", "icono": "📣",
        "intro": "Estrategias digitales, parrillas de contenido, campañas, redes sociales, "
                 "copywriting, producción audiovisual y comunicación de marca.",
    },
]


def proyecto(cat, n, titulo, anio, resumen, rol, herramientas, tipo, **extra):
    """Plantilla de proyecto. Reemplaza los textos y rutas por los tuyos."""
    base = {
        "id": f"{cat}-{n}", "cat": cat, "titulo": titulo, "anio": anio, "resumen": resumen,
        "tags": [rol, herramientas, tipo],
        "portada": f"assets/{cat}{n}_portada.png",
        "contexto": "Describe el contexto, el problema o necesidad y el objetivo del proyecto.",
        "proceso": [
            "Paso 1 · Investigación / exploración inicial.",
            "Paso 2 · Conceptualización y bocetos.",
            "Paso 3 · Desarrollo y diseño.",
            "Paso 4 · Pruebas, ajustes y entrega.",
        ],
        "fotos": [f"assets/{cat}{n}_{i}.png" for i in range(1, 5)],   # 4 fotos
        "video": f"assets/{cat}{n}_video.mp4",                         # 1 video
        "resultado": "Describe el resultado final y, si hay, métricas comprobables.",
        "aprendizajes": "¿Qué aprendiste? ¿Qué harías distinto?",
        "enlace": "",   # enlace externo opcional (Behance, Figma, YouTube...)
    }
    base.update(extra)
    return base


PROYECTOS = [
    # ── 3D ──
    proyecto("3d", 1, "Nombre del proyecto 3D · 1", "2025",
             "Breve descripción del entorno, objeto o experiencia inmersiva y su propósito.",
             "Modelado 3D", "Maya · Unity", "Experiencia inmersiva"),
    proyecto("3d", 2, "Nombre del proyecto 3D · 2", "2025",
             "Breve descripción del videojuego o entorno virtual y el reto que resolvía.",
             "Diseño y modelado", "Maya · Unity", "Videojuego"),
    # ── UX/UI ──
    proyecto("ux", 1, "LovePaws Mobile App & Website", "2025",
             "Diseño UX/UI de app móvil y sitio web para apoyar la adopción y las donaciones "
             "a favor de animales, con foco en una experiencia clara y emocional.",
             "UX/UI", "Figma", "Producto digital",
             portada="assets/lovepaws_portada.png",
             enlace="https://www.behance.net/"),
    proyecto("ux", 2, "Nombre del proyecto UX/UI · 2", "2025",
             "Breve descripción del producto digital, la necesidad y el público objetivo.",
             "UX/UI", "Figma", "Prototipo"),
    # ── Visual ──
    proyecto("visual", 1, "Nombre del proyecto visual · 1", "2025",
             "Breve descripción de la identidad, campaña o pieza y su objetivo de comunicación.",
             "Dirección creativa", "Illustrator · Photoshop", "Identidad visual"),
    proyecto("visual", 2, "Nombre del proyecto visual · 2", "2024",
             "Breve descripción de la propuesta gráfica, editorial o fotográfica.",
             "Diseño gráfico", "Photoshop · Illustrator", "Diseño editorial"),
    # ── Investigación ──
    proyecto("inv", 1, "Nombre de la investigación · 1", "2025",
             "Pregunta de investigación, público participante y principal hallazgo.",
             "Investigadora", "Encuestas · Entrevistas", "Investigación"),
    proyecto("inv", 2, "Nombre de la investigación · 2", "2024",
             "Pregunta de investigación, metodología y propuesta estratégica resultante.",
             "Investigadora", "Excel · Matrices", "Estrategia"),
    # ── Contenido ──
    proyecto("cont", 1, "Nombre del proyecto de contenido · 1", "2025",
             "Marca o contexto, objetivo de comunicación y estrategia implementada.",
             "Estrategia y contenido", "Premiere · CapCut", "Redes sociales"),
    proyecto("cont", 2, "Nombre del proyecto de contenido · 2", "2024",
             "Marca o contexto, parrilla de contenido y resultados obtenidos.",
             "Copywriting", "Figma · CapCut", "Campaña digital"),
]

# ══════════════════════════════════════════════════════════════
# 2. ESTILOS
# ══════════════════════════════════════════════════════════════
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=Inter:wght@400;500;600&display=swap');
:root{--ink:#1a1a1a;--muted:#5f5f66;--peach:#F6D5C3;--orange:#F28C6B;--violet:#6C5CE7;--bg:#fdfcfb;--card:#ffffff;--line:#e8e4e0}
@media (prefers-color-scheme: dark){
 :root{--ink:#f3f0ee;--muted:#b6b2b0;--peach:#3a2a24;--bg:#141414;--card:#1d1d1d;--line:#333}}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion: reduce){html{scroll-behavior:auto}*{animation:none!important;transition:none!important}}
.stApp{background:var(--bg);font-family:'Inter',sans-serif;color:var(--ink)}
header[data-testid="stHeader"]{display:none}
.block-container{padding-top:0!important;max-width:1100px}
h1,h2,h3{font-family:'Fraunces',serif!important;color:var(--ink)!important;letter-spacing:-.01em}
p,li,span,label{color:var(--ink)}
.nav{position:fixed;top:0;left:0;right:0;z-index:99999;display:flex;align-items:center;justify-content:space-between;
 padding:14px 4vw;background:color-mix(in srgb,var(--bg) 88%,transparent);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.nav .brand{font-family:'Fraunces',serif;font-weight:700;font-size:1.2rem;color:var(--ink);text-decoration:none}
.nav .links{display:flex;gap:22px;flex-wrap:wrap}
.nav .links a{color:var(--ink);text-decoration:none;font-weight:500;font-size:.92rem}
.nav .links a:hover{color:var(--violet)}
@media(max-width:700px){.nav .links{gap:12px}.nav .links a{font-size:.78rem}}
.anchor{position:relative;top:-80px;visibility:hidden}
.hero{position:relative;margin-top:0;height:92vh;min-height:520px;border-radius:0 0 28px 28px;overflow:hidden;
 display:flex;align-items:center;justify-content:center;text-align:center;
 background:linear-gradient(135deg,#F6D5C3,#d9c9ff);margin-left:calc(50% - 50vw);margin-right:calc(50% - 50vw);width:100vw}
.hero video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hero .veil{position:absolute;inset:0;background:rgba(0,0,0,.45)}
.hero .inner{position:relative;color:#fff;padding:0 6vw}
.hero h1{color:#fff!important;font-size:clamp(2.6rem,7vw,5rem);margin:0}
.hero .f{font-size:1.15rem;margin:.6rem 0 .2rem;color:#fff}
.hero .e{opacity:.9;margin-bottom:1.6rem;color:#fff}
.btn{display:inline-block;padding:12px 26px;border-radius:999px;font-weight:600;text-decoration:none!important;margin:5px;font-size:.95rem}
.btn.p{background:var(--orange);color:#fff!important}
.btn.s{background:transparent;color:#fff!important;border:1.5px solid #fff}
.sec{padding:80px 0 10px}
.eyebrow{font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);font-weight:600}
.chip{display:inline-block;background:var(--line);color:var(--ink);border-radius:999px;padding:5px 13px;margin:3px 6px 3px 0;font-size:.82rem;font-weight:500}
.cathead{display:flex;align-items:baseline;gap:12px;margin-top:38px}
.cathead .n{color:var(--muted);font-size:.9rem}
.meta{font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600;margin-top:10px}
.ptitle{font-family:'Fraunces',serif;font-size:1.45rem;font-weight:700;margin:4px 0 6px}
.ph{background:linear-gradient(135deg,var(--peach),#e9e3ff);border-radius:12px;display:flex;align-items:center;
 justify-content:center;color:#6b5b55;font-size:.85rem;text-align:center;padding:14px;aspect-ratio:16/10;width:100%}
div[data-testid="stVerticalBlockBorderWrapper"]{border-radius:18px!important;background:var(--card);border-color:var(--line)!important}
.flow{text-align:center;padding:18px 0}
.contact{background:#1a1a1a;border-radius:24px;padding:60px 6vw;text-align:center;margin-top:70px}
.contact h2,.contact p,.contact span{color:#fff!important}
.contact a.btn.p{background:var(--orange)}
.contact a.btn.s{color:#fff!important;border-color:#fff}
.footer{text-align:center;padding:40px 0 30px;color:var(--muted);font-size:.9rem}
.footer a{color:var(--muted);margin:0 8px}
.skillcard{border:1px solid var(--line);border-radius:16px;padding:18px;background:var(--card);height:100%}
.detail-top{padding-top:30px}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# 3. UTILIDADES
# ══════════════════════════════════════════════════════════════
def existe(src: str) -> bool:
    return bool(src) and (src.startswith("http") or Path(src).exists())


def mostrar_imagen(src: str, alt: str = ""):
    if existe(src):
        st.image(src, caption=None, use_container_width=True)
    else:
        st.markdown(f'<div class="ph" role="img" aria-label="{alt}">📷 Agrega tu imagen<br>{src}</div>',
                    unsafe_allow_html=True)


def mostrar_video(src: str):
    if existe(src):
        st.video(src)
    else:
        st.markdown(f'<div class="ph" role="img" aria-label="Video del proyecto">🎬 Agrega tu video<br>{src}</div>',
                    unsafe_allow_html=True)


def b64_video(path: str):
    p = Path(path)
    if p.exists() and p.stat().st_size < 15_000_000:
        return base64.b64encode(p.read_bytes()).decode()
    return None


def abrir(pid):
    st.session_state.proyecto = pid


def cerrar():
    st.session_state.proyecto = None


if "proyecto" not in st.session_state:
    st.session_state.proyecto = None

mail_href = f"mailto:{PERFIL['email']}?subject={quote('Hola Sara, me gustaría conversar')}"
wa_href = f"https://wa.me/{PERFIL['whatsapp']}?text={quote('Hola Sara, vi tu portafolio y me gustaría conversar.')}"


def bloque_contacto():
    st.markdown(f"""
    <div class="contact" id="contacto-box">
      <h2>¿Creamos algo juntos?</h2>
      <p>Conversemos sobre oportunidades laborales, proyectos y colaboraciones.</p>
      <p>📍 {PERFIL['ubicacion']} &nbsp;·&nbsp; ✉️ {PERFIL['email']} &nbsp;·&nbsp; 📞 {PERFIL['telefono']}</p>
      <a class="btn p" href="{mail_href}" target="_blank">✉️ Escríbeme al correo</a>
      <a class="btn s" href="{wa_href}" target="_blank">WhatsApp</a>
      <a class="btn s" href="{PERFIL['linkedin']}" target="_blank">LinkedIn</a>
    </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# 4A. PÁGINA DE DETALLE DE PROYECTO
# ══════════════════════════════════════════════════════════════
if st.session_state.proyecto:
    p = next(x for x in PROYECTOS if x["id"] == st.session_state.proyecto)
    cat = next(c for c in CATEGORIAS if c["id"] == p["cat"])

    st.markdown('<div class="detail-top"></div>', unsafe_allow_html=True)
    st.button("← Volver al portafolio", on_click=cerrar)

    st.markdown(f'<div class="meta">{cat["nombre"]} · {p["anio"]}</div>', unsafe_allow_html=True)
    st.title(p["titulo"])
    st.markdown("".join(f'<span class="chip">{t}</span>' for t in p["tags"]), unsafe_allow_html=True)
    mostrar_imagen(p["portada"], f"Imagen principal de {p['titulo']}")

    st.header("Descripción")
    st.write(p["resumen"])
    st.subheader("Contexto y objetivo")
    st.write(p["contexto"])

    st.header("Proceso")
    for i, paso in enumerate(p["proceso"], 1):
        st.markdown(f"**{i}.** {paso}")

    st.header("Galería")
    cols = st.columns(2)
    for i, foto in enumerate(p["fotos"][:4]):
        with cols[i % 2]:
            mostrar_imagen(foto, f"{p['titulo']} · imagen {i+1}")
            st.write("")

    st.header("Video")
    mostrar_video(p["video"])

    st.header("Resultado final")
    st.write(p["resultado"])
    st.subheader("Aprendizajes")
    st.write(p["aprendizajes"])

    if p["enlace"]:
        st.link_button("Ver proyecto externo ↗", p["enlace"])

    bloque_contacto()
    st.stop()

# ══════════════════════════════════════════════════════════════
# 4B. PÁGINA PRINCIPAL
# ══════════════════════════════════════════════════════════════
st.markdown(f"""
<nav class="nav" aria-label="Navegación principal">
  <a class="brand" href="#inicio" target="_self">{PERFIL['nombre']}</a>
  <div class="links">
    <a href="#inicio" target="_self">Inicio</a>
    <a href="#sobre-mi" target="_self">Sobre mí</a>
    <a href="#portafolio" target="_self">Portafolio</a>
    <a href="#hoja-de-vida" target="_self">Hoja de vida</a>
    <a href="#contactame" target="_self">Contáctame</a>
  </div>
</nav>
<div class="anchor" id="inicio"></div>
""", unsafe_allow_html=True)

# ── INICIO ──
vid = b64_video(PERFIL["hero_video"])
video_tag = (f'<video autoplay muted loop playsinline aria-hidden="true">'
             f'<source src="data:video/mp4;base64,{vid}" type="video/mp4"></video>') if vid else ""
st.markdown(f"""
<section class="hero">
  {video_tag}<div class="veil"></div>
  <div class="inner">
    <h1>{PERFIL['nombre']}</h1>
    <div class="f">{PERFIL['formacion']}</div>
    <div class="e">{PERFIL['especialidades']}</div>
    <a class="btn p" href="#portafolio" target="_self">Explorar portafolio</a>
    <a class="btn s" href="#sobre-mi" target="_self">Conocer mi perfil</a>
  </div>
</section>
""", unsafe_allow_html=True)

# ── SOBRE MÍ ──
st.markdown('<div class="anchor" id="sobre-mi"></div><div class="sec"></div>', unsafe_allow_html=True)
c1, c2 = st.columns([1, 2], gap="large")
with c1:
    mostrar_imagen(PERFIL["foto"], "Fotografía de Sara Londoño")
with c2:
    st.markdown('<div class="eyebrow">Sobre mí</div>', unsafe_allow_html=True)
    st.header("Comunicación + diseño interactivo")
    st.write(PERFIL["descripcion"])
    st.markdown('<a class="btn p" href="#hoja-de-vida" target="_self">Ver hoja de vida completa</a>',
                unsafe_allow_html=True)

st.write("")
cols = st.columns(2)
for i, (area, items) in enumerate(HABILIDADES.items()):
    with cols[i % 2]:
        chips = "".join(f'<span class="chip">{x}</span>' for x in items)
        st.markdown(f'<div class="skillcard"><b>{area}</b><br><br>{chips}</div><br>', unsafe_allow_html=True)

# ── PORTAFOLIO ──
st.markdown('<div class="anchor" id="portafolio"></div><div class="sec"></div>', unsafe_allow_html=True)
st.markdown('<div class="eyebrow">Portafolio</div>', unsafe_allow_html=True)
st.header("Proyectos por categoría")
st.write("Cada categoría contiene proyectos que abren sus propios casos de estudio.")

for cat in CATEGORIAS:
    proys = [x for x in PROYECTOS if x["cat"] == cat["id"]]
    st.markdown(f'<div class="cathead"><h3 style="margin:0">{cat["icono"]} {cat["nombre"]}</h3>'
                f'<span class="n">{len(proys)} proyectos</span></div>', unsafe_allow_html=True)
    st.write(cat["intro"])
    cols = st.columns(2, gap="large")
    for col, p in zip(cols, proys):
        with col:
            with st.container(border=True):
                mostrar_imagen(p["portada"], f"Portada de {p['titulo']}")
                st.markdown(
                    f'<div class="meta">{cat["nombre"]} · {p["anio"]}</div>'
                    f'<div class="ptitle">{p["titulo"]}</div>'
                    f'<p>{p["resumen"]}</p>'
                    + "".join(f'<span class="chip">{t}</span>' for t in p["tags"]),
                    unsafe_allow_html=True)
                st.button("Ver proyecto completo ↗", key=f"btn-{p['id']}",
                          on_click=abrir, args=(p["id"],), use_container_width=True)

# ── HOJA DE VIDA ──
st.markdown('<div class="anchor" id="hoja-de-vida"></div><div class="sec"></div>', unsafe_allow_html=True)
st.markdown('<div class="eyebrow">Hoja de vida</div>', unsafe_allow_html=True)
st.header("Trayectoria profesional")
a, b = st.columns([1, 2], gap="large")
with a:
    mostrar_imagen(PERFIL["foto"], "Fotografía de Sara Londoño")
    st.markdown(f"**Contacto**  \n{PERFIL['email']}  \n{PERFIL['telefono']}  \n{PERFIL['ubicacion']}")
    st.subheader("Idiomas")
    for idioma, nivel in HOJA_DE_VIDA["idiomas"]:
        st.markdown(f"**{idioma}** · {nivel}")
    cv = Path(PERFIL["cv_pdf"])
    if cv.exists():
        st.download_button("⬇ Descargar hoja de vida (PDF)", cv.read_bytes(),
                           file_name=cv.name, mime="application/pdf", use_container_width=True)
    else:
        st.info("Agrega tu PDF en assets/CV_Sara_Londono.pdf para activar la descarga.")
with b:
    st.subheader("Perfil profesional")
    st.write(HOJA_DE_VIDA["perfil"])
    st.subheader("Experiencia")
    for fecha, cargo, org, desc in HOJA_DE_VIDA["experiencia"]:
        st.markdown(f"**{cargo}** · {org}  \n<span class='eyebrow'>{fecha}</span>  \n{desc}",
                    unsafe_allow_html=True)
    st.subheader("Formación académica")
    for inst, titulo, anios in HOJA_DE_VIDA["formacion"]:
        st.markdown(f"**{titulo}** · {inst} ({anios})")
    st.subheader("Cursos y diplomados")
    for c in HOJA_DE_VIDA["cursos"]:
        st.markdown(f"- {c}")

# ── CONTÁCTAME ──
st.markdown('<div class="anchor" id="contactame"></div>', unsafe_allow_html=True)
bloque_contacto()

# ── PIE DE PÁGINA ──
st.markdown(f"""
<div class="footer">
  <b>{PERFIL['nombre']}</b><br>Diseño Interactivo · Comunicación Social<br>{PERFIL['ubicacion']}<br><br>
  <a href="{PERFIL['linkedin']}" target="_blank">LinkedIn</a>
  <a href="mailto:{PERFIL['email']}">Correo</a>
  <a href="#inicio" target="_self">Inicio</a>
  <a href="#sobre-mi" target="_self">Sobre mí</a>
  <a href="#portafolio" target="_self">Portafolio</a>
  <a href="#hoja-de-vida" target="_self">Hoja de vida</a>
</div>""", unsafe_allow_html=True)
