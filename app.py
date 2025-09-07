# Streamlit Cloud: EDA Airbnb NYC 
import os
import io
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="EDA Airbnb NYC", layout="wide")

@st.cache_data
def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

@st.cache_data
def load_csv_bytes(file_bytes: bytes) -> pd.DataFrame:
    return pd.read_csv(io.BytesIO(file_bytes))

def build_df_clean(df: pd.DataFrame) -> pd.DataFrame:
    df_clean = df.copy()
    # Imputaciones mínimas
    if "name" in df_clean.columns:
        df_clean["name"] = df_clean["name"].fillna("Desconocido")
    if "host_name" in df_clean.columns:
        df_clean["host_name"] = df_clean["host_name"].fillna("Desconocido")
    # Eliminar columnas no usadas con muchos nulos
    for col in ["last_review", "reviews_per_month"]:
        if col in df_clean.columns:
            df_clean.drop(columns=[col], inplace=True)
    return df_clean

def iqr_cap(s: pd.Series, k: float = 1.5) -> pd.Series:
    q1, q3 = s.quantile(0.25), s.quantile(0.75)
    iqr = q3 - q1
    low, high = q1 - k * iqr, q3 + k * iqr
    return s.clip(low, high)

# Sidebar
st.sidebar.title("Configuración de datos")

DEFAULTS = [
    "data/airbnb_clean.csv",
    "data/AB_NYC_2019.csv",
]

# Selector de origen
data_source = st.sidebar.radio(
    "Origen de datos",
    ["Archivo del repositorio", "Subir CSV"],
    index=0
)

df_clean = None
selected_path = None

if data_source == "Archivo del repositorio":
    # Intentamos rutas comunes del repositorio
    existing = [p for p in DEFAULTS if os.path.exists(p)]
    if existing:
        selected_path = st.sidebar.selectbox("Selecciona un archivo del repositorio", existing)
        try:
            df = load_csv(selected_path)
            df_clean = build_df_clean(df)
            st.sidebar.success(f"Archivo cargado: {selected_path} ({len(df_clean):,} filas)")
        except Exception as e:
            st.sidebar.error(f"No se pudo leer {selected_path}: {e}")
    else:
        st.sidebar.warning("No se encontró ningún CSV en data/. Sube un archivo en la opción siguiente")
else:
    up = st.sidebar.file_uploader("Sube tu CSV (Airbnb NYC u otro)", type=["csv"])
    if up is not None:
        try:
            df = load_csv_bytes(up.getvalue())
            df_clean = build_df_clean(df)
            st.sidebar.success(f"Archivo cargado: {up.name} ({len(df_clean):,} filas)")
        except Exception as e:
            st.sidebar.error(f"No se pudo leer el CSV subido: {e}")

if df_clean is None:
    st.stop()

# Filtros
st.sidebar.markdown("---")
room_types = sorted(df_clean["room_type"].dropna().unique()) if "room_type" in df_clean.columns else []
boroughs = sorted(df_clean["neighbourhood_group"].dropna().unique()) if "neighbourhood_group" in df_clean.columns else []

sel_rooms = st.sidebar.multiselect("Room type(s)", options=room_types, default=room_types)
sel_boroughs = st.sidebar.multiselect("Borough(s)", options=boroughs, default=boroughs)

min_price = float(df_clean["price"].min()) if "price" in df_clean.columns else 0.0
max_price = float(df_clean["price"].clip(upper=5000).max()) if "price" in df_clean.columns else 1000.0
price_range = st.sidebar.slider("Rango de precio ($)", min_value=0.0, max_value=max_price,
                                value=(0.0, min(500.0, max_price)), step=10.0)

# Aplicar filtros
df_view = df_clean.copy()
if sel_rooms and "room_type" in df_view.columns:
    df_view = df_view[df_view["room_type"].isin(sel_rooms)]
if sel_boroughs and "neighbourhood_group" in df_view.columns:
    df_view = df_view[df_view["neighbourhood_group"].isin(sel_boroughs)]
if "price" in df_view.columns:
    df_view = df_view[(df_view["price"] >= price_range[0]) & (df_view["price"] <= price_range[1])]

st.sidebar.info(f"Filas visibles: {len(df_view):,}")

# Header
st.title("Airbnb NYC - EDA Dashboard")
if selected_path:
    st.caption(f"Fuente: {selected_path}")
elif data_source == "Subir CSV":
    st.caption("Fuente: archivo subido por el usuario")
else:
    st.caption("Fuente: dataset")

# KPIs
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Filas (vista filtrada)", f"{len(df_view):,}")
with col2:
    if "price" in df_view.columns:
        st.metric("Precio mediano", f"${df_view['price'].median():.0f}")
with col3:
    if "price" in df_view.columns:
        st.metric("Precio promedio", f"${df_view['price'].mean():.0f}")
with col4:
    if "minimum_nights" in df_view.columns:
        st.metric("Min. noches (mediana)", f"{df_view['minimum_nights'].median():.0f}")

st.divider()

# Tabs de gráficos
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Distribución de precios",
    "Precio por tipo",
    "Top barrios",
    "Correlaciones",
    "Mapa"
])

with tab1:
    st.subheader("Distribución de precios")
    if "price" in df_view.columns:
        fig = px.histogram(df_view, x="price", nbins=50, opacity=0.9)
        fig.update_layout(xaxis_title="Precio", yaxis_title="Frecuencia")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No existe la columna 'price'")

with tab2:
    st.subheader("Precio por tipo de habitación (boxplot)")
    if {"room_type", "price"}.issubset(df_view.columns):
        temp = df_view.copy()
        temp["price_cap"] = iqr_cap(temp["price"])
        fig2 = px.box(temp, x="room_type", y="price_cap", points="suspectedoutliers",
                      category_orders={"room_type": list(room_types)})
        fig2.update_layout(xaxis_title="room_type", yaxis_title="price (cap IQR)")
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("Faltan columnas para este gráfico")

with tab3:
    st.subheader("Top 10 barrios por cantidad de alojamientos")
    if "neighbourhood" in df_view.columns:
        top10 = df_view["neighbourhood"].value_counts().head(10).sort_values(ascending=True)
        fig3 = px.bar(top10, orientation="h", labels={"value": "conteo", "index": "neighbourhood"})
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.info("No existe la columna 'neighbourhood'")

with tab4:
    st.subheader("Matriz de correlación (numéricas)")
    num_cols = [c for c in ["price", "minimum_nights", "number_of_reviews",
                            "calculated_host_listings_count", "availability_365"]
                if c in df_view.columns]
    if len(num_cols) >= 2:
        corr = df_view[num_cols].corr()
        fig4 = px.imshow(corr, text_auto=True, color_continuous_scale="RdBu", zmin=-1, zmax=1,
                         labels=dict(color="corr"))
        st.plotly_chart(fig4, use_container_width=True)
    else:
        st.info("No hay suficientes columnas numéricas para correlación")

with tab5:
    st.subheader("Mapa de alojamientos (muestra)")
    needed = {"latitude", "longitude"}.issubset(df_view.columns)
    if needed:
        sample_geo = df_view.sample(min(4000, len(df_view)), random_state=42)
        # Intento API; fallback a mapbox si no existe (según versión de plotly)
        try:
            fig5 = px.scatter_map(
                sample_geo,
                lat="latitude", lon="longitude",
                color="room_type" if "room_type" in sample_geo.columns else None,
                size="price" if "price" in sample_geo.columns else None,
                hover_name="name" if "name" in sample_geo.columns else None,
                hover_data={"neighbourhood": True} if "neighbourhood" in sample_geo.columns else None,
                zoom=10, height=650, map_style="carto-positron"
            )
        except Exception:
            fig5 = px.scatter_mapbox(
                sample_geo,
                lat="latitude", lon="longitude",
                color="room_type" if "room_type" in sample_geo.columns else None,
                size="price" if "price" in sample_geo.columns else None,
                hover_name="name" if "name" in sample_geo.columns else None,
                hover_data={"neighbourhood": True} if "neighbourhood" in sample_geo.columns else None,
                zoom=10, height=650, mapbox_style="carto-positron"
            )
        st.plotly_chart(fig5, use_container_width=True)
    else:
        st.info("No existen columnas 'latitude' y 'longitude' para el mapa")

st.divider()
st.caption("Datos: Airbnb NYC 2019. Dashboard con fines Educativos. Autor: Victor Saldivia Vera")
