import threading
import time

# Función que simula una actividad para mantener la app activa
def keep_awake():
    while True:
        time.sleep(600)  # Espera 10 minutos
        print("Manteniendo la app activa...")

# Inicia el hilo de actividad
thread = threading.Thread(target=keep_awake, daemon=True)
thread.start()

# Aquí comienza tu código original
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

# Continúa el resto de tu código...
