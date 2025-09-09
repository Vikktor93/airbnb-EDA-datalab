<p align="left">
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white" alt="Python 3.12.11">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License">
  </a>
  <img src="https://img.shields.io/badge/Notebook-Jupyter-orange?logo=jupyter" alt="Jupyter Notebooks">
  <img src="https://img.shields.io/badge/App-Streamlit-red?logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/EDA-Exploratory%20Data%20Analysis-blueviolet" alt="EDA Project">
  <a href="https://airbnb-2019-eda.streamlit.app/">
    <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Open in Streamlit">
  </a>
  <img src="./assets/EDA-Dashboard.gif"/>
</p>

# EDA Airbnb NYC 2019 - Mini Proyecto DataLab

Este proyecto corresponde a un **Análisis Exploratorio de Datos (EDA)** desarrollado en Python como parte del curso **Python para Data Science de DataLab**.  Este trabajo utiliza el dataset **Airbnb NYC 2019** (disponible en [Kaggle](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data)).

## 🚀 Demo en línea | Live Demo

Puedes visualizar el Dashboard directamente aquí:  
👉 [**Abrir en Streamlit Cloud**](https://airbnb-2019-eda.streamlit.app/)


### Objetivos de Aprendizaje

- Aplicar técnicas de limpieza de datos (manejo de nulos y eliminación de columnas irrelevantes).  
- Analizar variables categóricas y numéricas mediante visualizaciones.  
- Identificar y tratar outliers.  
- Realizar análisis geográfico interactivo con Plotly.  
- Interpretar correlaciones entre variables numéricas.  
- Comunicar hallazgos mediante insights y conclusiones claras.


### Estructura del proyecto

```bash
Mini-Proyecto/
│
├── data/                      # Datasets originales y procesados | Original and processed datasets
│   ├── AB_NYC_2019.csv
│   ├── airbnb_cap.csv
│   ├── airbnb_clean.csv
│   ├── archive.zip
│   └── New_York_City_.png
│
├── output/                    # Gráficos generados | Generated plots
│   ├── boxplot_outliers.png
│   ├── boxplot_precios.png
│   ├── distribucion_minimum_nights.png
│   ├── distribucion_precios.png
│   ├── distribucion_room_type.png
│   ├── heatmap_corr.png
│   ├── mapa_airbnb.png
│   ├── precio_promedio_room_type.png
│   └── top10_barrios.png
│
├── 000_instrucciones.ipynb    # Notebook con instrucciones | Instructions notebook
├── 001_EDA.ipynb              # Notebook principal del EDA | Main EDA notebook
│
├── LICENSE                    # Licencia | License
└── README.md                  # Documentación | Documentation
```
### Instalación y Requisitos

Este proyecto está pensado para ejecutarse en Python 3.12.11 con Anaconda.
Las principales librerías utilizadas son:
- `numpy == 1.26.4`
- `pandas == 2.3.1`
- `matplotlib == 3.10.1`
- `seaborn == 0.13.2`
- `plotly == 6.0.1`
- `kaleido == 0.2.1`
- `geopandas == 1.0.1` (opcional, para análisis geoespacial más avanzado)


Instalación con conda

Para instalar todas las dependencias, utiliza el archivo `requirements.txt`:

```bash
conda create -n eda_airbnb python=3.12.11
conda activate eda_airbnb
pip install -r requirements.txt
```
Instalación con pip
```bash
pip install -r requirements.txt
```

Ejecución

1. Clona este repositorio:
    ```bash
    git clone https://github.com/Vikktor93/airbnb-EDA-datalab
    cd EDA_Airbnb
    ```

2. Abrir el repositorio en VS Code
3. Ejecuta cada celda paso a paso.

    Los gráficos se guardarán automáticamente en la carpeta `output/.`

### Outputs principales

- Distribución por tipo de habitación.
- Precio promedio por tipo de habitación.
- Top 10 barrios con más alojamientos.
- Distribución de precios (con y sin outliers).
- Distribución de minimum_nights.
- Boxplots comparativos de precios.
- Heatmap de correlaciones.
- Mapa interactivo de alojamientos en NYC.

### Insights preliminares

- El tipo de habitación y la ubicación son factores clave en el precio.
- La mayoría de los alojamientos cuesta menos de $500 USD, aunque existen outliers extremos.
- Los mínimos de noches suelen estar entre 1 y 5, pero hay valores irreales que requieren limpieza.
- Los barrios más concentrados son Manhattan y Brooklyn, con precios más altos en zonas céntricas.
- Las correlaciones entre variables numéricas son bajas, lo que muestra que factores categóricos son más explicativos.

### Licencia

Este proyecto se distribuye bajo la [licencia MIT](https://github.com/Vikktor93/airbnb-EDA-datalab/blob/main/LICENSE).
Puedes reutilizar y adaptar el material con fines educativos o personales, siempre nombrando al autor original del repositorio.