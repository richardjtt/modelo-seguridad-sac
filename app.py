import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuración inicial de la página (Debe ser la primera instrucción)
st.set_page_config(
    page_title="Plataforma de Gestión Estratégica - Seguridad Privada",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo visual personalizado mediante CSS global
st.markdown("""
    <style>
    .main-header { font-size: 28px; font-weight: 800; color: #1E3A8A; margin-bottom: 5px;}
    .sub-header { font-size: 18px; font-weight: bold; color: #0F172A; margin-top: 20px; }
    .subtitle { font-size: 16px; color: #64748B; margin-bottom: 30px; }
    .card { background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); border-top: 4px solid #2563EB; height: 100%; }
    .card-title { font-size: 18px; font-weight: 700; color: #1E3A8A; margin-bottom: 10px; }
    .card-text { font-size: 14px; color: #334155; line-height: 1.5; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# MENÚ DE NAVEGACIÓN LATERAL
# ==========================================
st.sidebar.title("📌 Navegación")
# Se coloca la Propuesta Estratégica como la primera opción para que cargue por defecto
opcion_menu = st.sidebar.radio(
    "Seleccione el módulo a visualizar:",
    ["🚀 Propuesta Estratégica (Roadmap)", "📊 Modelo Financiero y Costos"]
)
st.sidebar.markdown("---")


# ==========================================
# VISTA 1: PROPUESTA ESTRATÉGICA (ROADMAP) - INICIA POR DEFECTO
# ==========================================
if opcion_menu == "🚀 Propuesta Estratégica (Roadmap)":
    
    st.markdown('<div class="main-header" style="text-align: center;">🚀 Plan de Transformación Financiera y Operativa para Seguridad Privada</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle" style="text-align: center;">Evolucionando de la operatividad manual a la inteligencia predictiva impulsada por datos</div>', unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("### 🗺️ Visión Estratégica: Esquema de Trabajo")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-title">1. Modelo y Estructura de Costos</div>
            <div class="card-text">
                Actualización del modelo corporativo para definir objetivos claros. Estructuración del Estado de Resultados (EERR) y alineación de costos para calcular, analizar y maximizar la rentabilidad.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-title">2. Bases de Datos y Organización</div>
            <div class="card-text">
                Construcción de bases de datos operativas y financieras bien organizadas. Creación de un modelo sólido que permita extraer y consultar datos de forma dinámica, eficiente y centralizada.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <div class="card-title">3. Automatización de Procesos</div>
            <div class="card-text">
                Identificación de cuellos de botella y mejora de procesos. Automatización de flujos de trabajo rutinarios para reducir la carga administrativa manual, permitiendo un enfoque total en la gestión.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card">
            <div class="card-title">4. Inteligencia Artificial (IA)</div>
            <div class="card-text">
                Análisis de predicción financiera y operativa mediante Machine Learning. Solución de problemas internos y desarrollo de servicios Sub-IA al cliente para incrementar la calidad y competitividad.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    st.markdown("### 📈 Secuencia de Objetivos y Flujo de Implementación")
    
    # Diagrama de flujo secuencial (Gantt sin fechas, usando barras horizontales con bases)
    df_secuencia = pd.DataFrame([
        dict(Fase="1. Modelo Financiero y Costos", Inicio=0, Fin=2, Objetivo="Rentabilidad Transparente"),
        dict(Fase="2. Organización de Bases de Datos", Inicio=1, Fin=3.5, Objetivo="Información Centralizada"),
        dict(Fase="3. Automatización de Procesos", Inicio=2.5, Fin=5.5, Objetivo="Eficiencia Operativa"),
        dict(Fase="4. Modelos Predictivos Internos", Inicio=4.5, Fin=7.5, Objetivo="Analítica y Predicción"),
        dict(Fase="5. Servicios IA al Cliente", Inicio=6, Fin=9, Objetivo="Expansión de Portafolio")
    ])
    df_secuencia["Duracion"] = df_secuencia["Fin"] - df_secuencia["Inicio"]

    fig_secuencia = px.bar(
        df_secuencia, 
        x="Duracion", 
        y="Fase", 
        base="Inicio",
        color="Objetivo", 
        orientation='h',
        text="Objetivo",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig_secuencia.update_yaxes(autorange="reversed", title="")
    # Ocultar completamente el eje X para que no parezca un calendario/cronograma con topes
    fig_secuencia.update_xaxes(showticklabels=False, showgrid=False, zeroline=False, title="")
    fig_secuencia.update_traces(hovertemplate="<b>%{y}</b><br>Objetivo: %{text}<extra></extra>")
    fig_secuencia.update_layout(
        height=350, 
        margin=dict(t=20, b=10, l=10, r=10), 
        plot_bgcolor="rgba(0,0,0,0)", 
        paper_bgcolor="rgba(0,0,0,0)",
        showlegend=False
    )
    st.plotly_chart(fig_secuencia, use_container_width=True)

    st.markdown("---")
    st.markdown("### 🎯 El Objetivo Final: Una Empresa Gestionada por Datos")
    st.write("La consolidación de esta propuesta transforma la empresa, pasando de una operación tradicional a una organización tecnológica que garantiza calidad de servicio y rentabilidad.")

    df_funnel = pd.DataFrame(dict(
        number=[100, 70, 45, 20],
        stage=["Operación Tradicional Manual", "Toma de Decisiones Basada en Datos", "Operación Automatizada y Eficiente", "Empresa Predictiva Impulsada por IA"]
    ))
    fig_funnel = px.funnel(df_funnel, x='number', y='stage')
    fig_funnel.update_layout(showlegend=False, margin=dict(t=20, b=20), height=300)

    col_f1, col_f2 = st.columns([1.5, 1])

    with col_f1:
        st.plotly_chart(fig_funnel, use_container_width=True)

    with col_f2:
        st.markdown("#### 📊 Impacto Proyectado")
        st.metric(label="Reducción de Carga Administrativa Manual", value="Alta", delta="Enfoque en Gestión")
        st.metric(label="Precisión en Extracción de Datos", value="Dinámica", delta="Decisiones Rápidas")
        st.metric(label="Competitividad en el Mercado", value="Superior", delta="Nuevos Servicios IA", delta_color="normal")
        st.info("💡 **Resultado:** Una compañía escalable, con procesos automatizados, control total del área financiera y lista para implementar Inteligencia Artificial en sus servicios.")


# ==========================================
# VISTA 2: MODELO FINANCIERO Y COSTOS
# ==========================================
elif opcion_menu == "📊 Modelo Financiero y Costos":
    
    st.markdown('<div class="main-header">🛡️ Modelo de Estructura de Costos y Gestión Financiera</div>', unsafe_allow_html=True)
    st.caption("Sector de Seguridad Privada en el Perú (Régimen General D.L. 728) - Optimizado para Análisis Masivo y Toma de Decisiones")

    # Parámetros del Modelo en la barra lateral
    st.sidebar.header("⚙️ Parámetros del Modelo")

    st.sidebar.subheader("1. Margen Comercial sobre el Costo")
    markup_costo_pct = st.sidebar.number_input(
        "% Margen Bruto (Mark-up)", 
        min_value=0.0, 
        max_value=100.0, 
        value=30.0, 
        step=1.0,
        help="Porcentaje que se adiciona sobre el Costo Operativo Directo para determinar los Ingresos (Ventas Netas)."
    ) / 100.0

    st.sidebar.markdown("---")
    st.sidebar.subheader("2. Personal Operativo (Agentes)")
    sueldo_agente = st.sidebar.number_input("Sueldo Base Agente (S/)", min_value=1025.0, value=2200.0, step=50.0)
    cant_agentes = st.sidebar.number_input("Cantidad de Agentes", min_value=1, value=800, step=10)

    st.sidebar.markdown("---")
    st.sidebar.subheader("3. Personal Administrativo (Estructura)")
    sueldo_admin = st.sidebar.number_input("Sueldo Base Administrativo (S/)", min_value=1025.0, value=4000.0, step=100.0)
    cant_admin = st.sidebar.number_input("Cantidad de Administrativos", min_value=1, value=100, step=5)

    st.sidebar.markdown("---")
    st.sidebar.subheader("4. Costos Fijos e Infraestructura (S/ Mensual)")
    costo_alquiler = st.sidebar.number_input("Alquiler de Sedes y Central de Control", min_value=0.0, value=95000.0, step=1000.0)
    costo_servicios = st.sidebar.number_input("Servicios Básicos (Luz, Agua, Telecom)", min_value=0.0, value=55000.0, step=1000.0)
    costo_equipos = st.sidebar.number_input("Equipamiento, Uniformes y Armamento", min_value=0.0, value=120000.0, step=5000.0)
    costo_supervision = st.sidebar.number_input("Supervisión Móvil, Vehículos y Combustible", min_value=0.0, value=135000.0, step=5000.0)
    costo_sucamec = st.sidebar.number_input("Acreditaciones SUCAMEC y Capacitación", min_value=0.0, value=48000.0, step=1000.0)
    costo_varios_admin = st.sidebar.number_input("Gastos Comerciales, Legales y Auditoría", min_value=0.0, value=78000.0, step=1000.0)
    depreciacion_mensual = st.sidebar.number_input("Depreciación Mensual (Para EBIT)", min_value=0.0, value=25000.0, step=1000.0)

    # Motor de Cálculo Laboral
    def calcular_costo_laboral_unitario(sueldo_base, es_agente=True):
        asig_fam = 56.50
        base_computable = sueldo_base + asig_fam
        
        essalud = base_computable * 0.09
        gratificacion = base_computable * (1.0 / 6.0)
        bono_extra = gratificacion * 0.09
        cts = (base_computable + (base_computable / 6.0)) / 12.0
        vacaciones = base_computable / 12.0
        
        pct_sctr = 0.017 if es_agente else 0.005
        pct_vida = 0.005 if es_agente else 0.004
        
        sctr = base_computable * pct_sctr
        vida_ley = base_computable * pct_vida
        
        total_sobrecostos = essalud + gratificacion + bono_extra + cts + vacaciones + sctr + vida_ley
        costo_total_unitario = base_computable + total_sobrecostos
        
        return {
            "Sueldo Bruto Promedio Base": sueldo_base,
            "Asignación Familiar (50% elegibilidad)": asig_fam,
            "Base Computable Promedio": base_computable,
            "EsSalud (Aporte Patronal 9.0%)": essalud,
            "Provisión Gratificación (Julio y Diciembre)": gratificacion,
            "Bonificación Extraordinaria (Ley 29351 - 9% s/ Grat)": bono_extra,
            "Provisión CTS (Incluye 1/6 Gratificación)": cts,
            "Provisión Vacaciones Anuales (30 días)": vacaciones,
            "SCTR (Salud y Pensión)": sctr,
            "Seguro de Vida Ley (D.L. 688)": vida_ley,
            "Total Sobrecostos Laborales Mensuales": total_sobrecostos,
            "Costo Laboral Total Mensual por Trabajador": costo_total_unitario
        }

    res_agente = calcular_costo_laboral_unitario(sueldo_agente, es_agente=True)
    res_admin = calcular_costo_laboral_unitario(sueldo_admin, es_agente=False)

    total_planilla_agentes = res_agente["Costo Laboral Total Mensual por Trabajador"] * cant_agentes
    total_planilla_admin = res_admin["Costo Laboral Total Mensual por Trabajador"] * cant_admin

    total_costo_operativo = total_planilla_agentes + costo_equipos + costo_supervision + costo_sucamec
    total_costo_estructura = total_planilla_admin + costo_alquiler + costo_servicios + costo_varios_admin
    gran_total_mensual = total_costo_operativo + total_costo_estructura
    gran_total_anual = gran_total_mensual * 12

    ingresos_mensuales = total_costo_operativo * (1.0 + markup_costo_pct)
    utilidad_bruta = ingresos_mensuales - total_costo_operativo
    ebitda_mensual = utilidad_bruta - total_costo_estructura
    ebit_mensual = ebitda_mensual - depreciacion_mensual
    impuesto_renta = ebit_mensual * 0.295 if ebit_mensual > 0 else 0.0
    utilidad_neta = ebit_mensual - impuesto_renta
    margen_neto_pct = (utilidad_neta / ingresos_mensuales) * 100 if ingresos_mensuales > 0 else 0

    # KPIs Principales
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        st.metric("Gran Total Costos Mensuales", f"S/ {gran_total_mensual:,.2f}", f"Anual: S/ {gran_total_anual:,.2f}")
    with kpi2:
        st.metric("Total Costo Operativo", f"S/ {total_costo_operativo:,.2f}", f"{(total_costo_operativo/gran_total_mensual)*100:.1f}% del Total de Costos")
    with kpi3:
        st.metric("Total Estructura (Admin + Fijos)", f"S/ {total_costo_estructura:,.2f}", f"{(total_costo_estructura/gran_total_mensual)*100:.1f}% del Total de Costos", delta_color="inverse")
    with kpi4:
        costo_puesto_prom = gran_total_mensual / cant_agentes if cant_agentes > 0 else 0
        st.metric("Costo Total Cargado / Puesto", f"S/ {costo_puesto_prom:,.2f}", help="Costo mensual total dividido entre la cantidad de agentes")

    st.markdown("---")

    # Matriz Sobrecostos
    st.markdown('<div class="sub-header">📊 Matriz de Sobrecostos Laborales y Beneficios Sociales por Puesto</div>', unsafe_allow_html=True)
    df_comparativo = pd.DataFrame({
        "Concepto de Costo Laboral / Beneficio": list(res_agente.keys()),
        "Agente Seguridad (S/)": list(res_agente.values()),
        "% s/ Base Agente": [ (v / sueldo_agente) * 100 for v in res_agente.values() ],
        "Personal Admin. (S/)": list(res_admin.values()),
        "% s/ Base Admin": [ (v / sueldo_admin) * 100 for v in res_admin.values() ]
    })
    df_formatted = df_comparativo.copy()
    df_formatted["Agente Seguridad (S/)"] = df_formatted["Agente Seguridad (S/)"].map("S/ {:,.2f}".format)
    df_formatted["% s/ Base Agente"] = df_formatted["% s/ Base Agente"].map("{:.2f}%".format)
    df_formatted["Personal Admin. (S/)"] = df_formatted["Personal Admin. (S/)"].map("S/ {:,.2f}".format)
    df_formatted["% s/ Base Admin"] = df_formatted["% s/ Base Admin"].map("{:.2f}%".format)
    st.dataframe(df_formatted, use_container_width=True, hide_index=True)

    # Consolidación Costos
    st.markdown('<div class="sub-header">🏢 Consolidación Estructural y Operativa</div>', unsafe_allow_html=True)
    col_left, col_right = st.columns([1.2, 0.8])
    with col_left:
        st.markdown("#### Desglose de Gastos por Categoría")
        resumen_data = {
            "Categoría de Costo": ["Planilla Directa Agentes", "Logística y Operativa Adicional", "Planilla Administrativa", "Gastos Fijos de Estructura"],
            "Tipo": ["Operativo", "Operativo", "Estructura Admin", "Estructura Admin"],
            "Monto Mensual (S/)": [total_planilla_agentes, costo_equipos + costo_supervision + costo_sucamec, total_planilla_admin, costo_alquiler + costo_servicios + costo_varios_admin]
        }
        df_resumen = pd.DataFrame(resumen_data)
        df_resumen["% del Total"] = (df_resumen["Monto Mensual (S/)"] / gran_total_mensual) * 100
        df_resumen["Monto Anual (S/)"] = df_resumen["Monto Mensual (S/)"] * 12
        df_resumen_view = df_resumen.copy()
        df_resumen_view["Monto Mensual (S/)"] = df_resumen_view["Monto Mensual (S/)"].map("S/ {:,.2f}".format)
        df_resumen_view["Monto Anual (S/)"] = df_resumen_view["Monto Anual (S/)"].map("S/ {:,.2f}".format)
        df_resumen_view["% del Total"] = df_resumen_view["% del Total"].map("{:.2f}%".format)
        st.dataframe(df_resumen_view, use_container_width=True, hide_index=True)

    with col_right:
        st.markdown("#### Distribución de la Carga de Costos")
        fig = px.pie(df_resumen, names="Categoría de Costo", values="Monto Mensual (S/)", hole=0.45, color_discrete_sequence=px.colors.qualitative.Set2)
        fig.update_layout(margin=dict(t=10, b=10, l=10, r=10), showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # EERR
    st.markdown('<div class="sub-header">📈 Estado de Resultados Proyectado (EERR)</div>', unsafe_allow_html=True)
    fin1, fin2, fin3, fin4 = st.columns(4)
    fin1.metric("Ventas Netas Mensuales", f"S/ {ingresos_mensuales:,.2f}")
    fin2.metric("Utilidad Bruta", f"S/ {utilidad_bruta:,.2f}", f"Margen Bruto: {(utilidad_bruta/ingresos_mensuales)*100:.1f}%")
    fin3.metric("EBITDA", f"S/ {ebitda_mensual:,.2f}", f"Margen EBITDA: {(ebitda_mensual/ingresos_mensuales)*100:.1f}%")
    fin4.metric("Utilidad Neta", f"S/ {utilidad_neta:,.2f}", f"Margen Neto: {margen_neto_pct:.1f}%")

    st.markdown("#### Detalle del EERR")
    eerr_data = {
        "Concepto Financiero": ["VENTAS NETAS TOTALES", "(-) Costo Operativo de Ventas", "(=) UTILIDAD BRUTA", "(-) Gastos de Administración y Ventas", "(=) EBITDA", "(-) Depreciación", "(=) UTILIDAD OPERATIVA (EBIT)", "(-) Impuesto a la Renta (29.5%)", "(=) UTILIDAD NETA DEL EJERCICIO"],
        "Monto Mensual (S/)": [ingresos_mensuales, -total_costo_operativo, utilidad_bruta, -total_costo_estructura, ebitda_mensual, -depreciacion_mensual, ebit_mensual, -impuesto_renta, utilidad_neta],
        "% s/ Ventas": [100.0, -(total_costo_operativo / ingresos_mensuales) * 100, (utilidad_bruta / ingresos_mensuales) * 100, -(total_costo_estructura / ingresos_mensuales) * 100, (ebitda_mensual / ingresos_mensuales) * 100, -(depreciacion_mensual / ingresos_mensuales) * 100, (ebit_mensual / ingresos_mensuales) * 100, -(impuesto_renta / ingresos_mensuales) * 100, margen_neto_pct]
    }
    df_eerr = pd.DataFrame(eerr_data)
    df_eerr_view = df_eerr.copy()
    df_eerr_view["Monto Mensual (S/)"] = df_eerr_view["Monto Mensual (S/)"].map("S/ {:,.2f}".format)
    df_eerr_view["% s/ Ventas"] = df_eerr_view["% s/ Ventas"].map("{:.2f}%".format)
    st.dataframe(df_eerr_view, use_container_width=True, hide_index=True)

    csv_data = df_comparativo.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Descargar Reporte Base en CSV", data=csv_data, file_name="estructura_costos_seguridad_privada.csv", mime="text/csv")