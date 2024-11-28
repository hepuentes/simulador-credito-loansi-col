import streamlit as st

# Función para formatear números con separadores de miles
def format_number(number):
    return "{:,.0f}".format(number).replace(",", ".")

# Datos para cada línea de crédito
LINEAS_DE_CREDITO = {
    "LoansiFlex": {
        "descripcion": "Crédito de libre inversión para empleados, independientes, personas naturales y pensionados.",
        "monto_min": 1000000,
        "monto_max": 20000000,
        "plazo_min": 12,
        "plazo_max": 60,
        "tasa_mensual": 1.9715,
        "tasa_anual_efectiva": 26.4,
        "aval_porcentaje": 0.10,
        "seguro_vida_base": 150000
    },
    "Microflex": {
        "descripcion": "Crédito rotativo para personas en sectores informales, orientado a cubrir necesidades de liquidez rápida con pagos semanales.",
        "monto_min": 50000,
        "monto_max": 500000,
        "plazo_min": 4,
        "plazo_max": 8,
        "tasa_mensual": 2.0718,
        "tasa_anual_efectiva": 27.9,
        "aval_porcentaje": 0.12,
    }
}

COSTOS_ASOCIADOS = {
    "Pagaré Digital": 2800,
    "Carta de Instrucción": 2800,
    "Custodia TVE": 5600,
    "Consulta Datacrédito": 11000
}

total_costos_asociados = sum(COSTOS_ASOCIADOS.values())

def calcular_seguro_vida(plazo, seguro_vida_base):
    años = plazo // 12
    return seguro_vida_base * años if años >= 1 else 0

# Estilos
st.markdown("""
    <style>
        .stSelectbox {
            margin-top: 0.2rem !important;
        }
        
        .stSelectbox > div > div {
            pointer-events: auto;
            background-color: #2D2D2D !important;
            border: 1px solid #404040 !important;
            color: #FFFFFF !important;
            cursor: pointer;
        }

        .description-text {
            color: #B0B0B0 !important;
            font-size: 1.1rem !important;
            margin: 0.8rem 0 !important;
            line-height: 1.4 !important;
        }

        .value-description {
            color: #B0B0B0 !important;
            font-size: 1.1rem !important;
            margin: 0.5rem 0 !important;
        }

        .plazo-text {
            color: #FFFFFF !important;
            font-size: 1.2rem !important;
            font-weight: 600 !important;
            margin-bottom: 0.5rem !important;
        }

        .stSlider > div > div > div {
            font-size: 1.2rem !important;
        }

        .currency-symbol {
            font-size: 1.3rem;
            color: #FFFFFF;
            margin-top: 0.7rem;
            margin-left: 0.2rem;
        }

        .result-box {
            background-color: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1.5rem 0;
            text-align: center;
        }
        
        .result-text {
            font-size: 1.2rem;
            color: #B0B0B0;
            margin-bottom: 0.8rem;
        }
        
        .result-amount {
            font-size: 2.2rem;
            font-weight: 700;
            color: #FFFFFF !important;
            text-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }

        .detail-item {
            display: flex;
            justify-content: space-between;
            padding: 0.75rem 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .detail-label {
            color: #B0B0B0;
        }
        
        .detail-value {
            color: #FFFFFF;
            font-weight: 500;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>Simulador de Crédito Loansi</h1>", unsafe_allow_html=True)

# Selección de línea de crédito
st.markdown("<p style='color: #FFFFFF; font-size: 1.4rem; font-weight: 700; margin-bottom: 0.2rem;'>Selecciona la Línea de Crédito</p>", unsafe_allow_html=True)
tipo_credito = st.selectbox("", options=LINEAS_DE_CREDITO.keys(), index=0, key="select_credito")
detalles = LINEAS_DE_CREDITO[tipo_credito]

st.markdown(f"<p class='description-text'>{detalles['descripcion']}</p>", unsafe_allow_html=True)

# Entrada del monto con símbolo de peso
st.markdown("<p style='color: #FFFFFF; font-size: 1.4rem; font-weight: 700; margin: 1.5rem 0 0.2rem;'>Escribe el valor del crédito</p>", unsafe_allow_html=True)
st.markdown(f"<p class='value-description'>Ingresa un valor entre $ {format_number(detalles['monto_min'])} y $ {format_number(detalles['monto_max'])} COP</p>", unsafe_allow_html=True)

col1, col2 = st.columns([0.5,20])
with col1:
    st.markdown('<div class="currency-symbol">$</div>', unsafe_allow_html=True)
with col2:
    monto = st.number_input("", 
                           min_value=detalles["monto_min"],
                           max_value=detalles["monto_max"],
                           step=1000,
                           format="%d",
                           key="monto_input")

# Slider de plazo con estilo mejorado
if tipo_credito == "LoansiFlex":
    st.markdown("<p class='plazo-text'>Plazo en Meses</p>", unsafe_allow_html=True)
    plazo = st.slider("", 
                     min_value=detalles["plazo_min"], 
                     max_value=detalles["plazo_max"], 
                     step=12,
                     key="slider_meses")
    frecuencia_pago = "Mensual"
else:
    st.markdown("<p class='plazo-text'>Plazo en Semanas</p>", unsafe_allow_html=True)
    plazo = st.slider("", 
                     min_value=detalles["plazo_min"], 
                     max_value=detalles["plazo_max"], 
                     step=1,
                     key="slider_semanas")
    frecuencia_pago = "Semanal"

# Cálculos
aval = monto * detalles["aval_porcentaje"]
seguro_vida = calcular_seguro_vida(plazo, detalles.get("seguro_vida_base", 0)) if tipo_credito == "LoansiFlex" else 0
total_financiar = monto + aval + total_costos_asociados + seguro_vida

# Cálculo de cuota
if tipo_credito == "LoansiFlex":
    cuota = (total_financiar * (detalles["tasa_mensual"] / 100)) / (1 - (1 + detalles["tasa_mensual"] / 100) ** -plazo)
else:
    tasa_mensual = detalles["tasa_mensual"] / 100
    tasa_semanal = ((1 + tasa_mensual) ** 0.25) - 1
    cuota = round((total_financiar * tasa_semanal) / (1 - (1 + tasa_semanal) ** -plazo))

# Mostrar resultado con orden invertido
st.markdown(f"""
<div class="result-box">
    <p class="result-text">Pagarás {plazo} cuotas por un valor aproximado de:</p>
    <div class="result-amount">$ {format_number(cuota)} {frecuencia_pago}</div>
</div>
""", unsafe_allow_html=True)

# Detalles del crédito
with st.expander("Ver Detalles del Crédito"):
    total_interes = cuota * plazo - total_financiar
    total_pagar = cuota * plazo
    
    detalles_orden = [
        ("Monto Solicitado", f"$ {format_number(monto)} COP"),
        ("Plazo", f"{plazo} {'meses' if tipo_credito == 'LoansiFlex' else 'semanas'}"),
        ("Frecuencia de Pago", frecuencia_pago),
        ("Tasa de Interés Mensual", f"{detalles['tasa_mensual']}%"),
        ("Tasa Efectiva Anual (E.A.)", f"{detalles['tasa_anual_efectiva']}%"),
        ("Costo del Aval", f"$ {format_number(aval)} COP"),
        ("Costos Asociados", f"$ {format_number(total_costos_asociados)} COP"),
    ]
    
    if tipo_credito == "LoansiFlex":
        detalles_orden.append(("Seguro de Vida", f"$ {format_number(seguro_vida)} COP"))
    
    detalles_orden.extend([
        ("Total Intereses", f"$ {format_number(total_interes)} COP"),
        ("Total a Pagar", f"$ {format_number(total_pagar)} COP")
    ])
    
    for titulo, valor in detalles_orden:
        st.markdown(f"""
        <div class="detail-item">
            <span class="detail-label">{titulo}</span>
            <span class="detail-value">{valor}</span>
        </div>
        """, unsafe_allow_html=True)
