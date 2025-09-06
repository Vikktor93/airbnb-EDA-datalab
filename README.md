# EDA Airbnb NYC 2019 - Mini Proyecto DataLab

Este proyecto corresponde a un **Análisis Exploratorio de Datos (EDA)** desarrollado en Python como parte del curso **Python para Data Science de DataLab**.  
Este trabajo utiliza el dataset **Airbnb NYC 2019** (disponible en [Kaggle](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data)).

### Objetivos de Aprendizaje

- Aplicar técnicas de limpieza de datos (manejo de nulos y eliminación de columnas irrelevantes).  
- Analizar variables categóricas y numéricas mediante visualizaciones.  
- Identificar y tratar outliers.  
- Realizar análisis geográfico interactivo con Plotly.  
- Interpretar correlaciones entre variables numéricas.  
- Comunicar hallazgos mediante insights y conclusiones claras.


### Estructura del proyecto

```bash
EDA_Airbnb/
│
├── data/                # Dataset original
├── notebooks/           # Jupyter Notebooks del análisis
│   └── EDA_Airbnb.ipynb
├── output/              # Gráficos generados 
│   ├── distribucion_room_type.png
│   ├── precio_promedio_room_type.png
│   ├── top10_barrios.png
│   ├── distribucion_precios.png
│   ├── boxplot_precios.png
│   ├── distribucion_minimum_nights.png
│   ├── mapa_airbnb.png
│   ├── heatmap_corr.png
│   └── boxplot_outliers.png
└── README.md
```
### Instalación y Requisitos

Este proyecto está pensado para ejecutarse en Python 3.12.11 con Anaconda.
Las principales librerías utilizadas son:
- `numpy == 1.26.4`
- `pandas == 2.3.1`
- `matplotlib == 3.10.1`
- `seaborn == 0.13.2`
- `plotly == 6.0.1`
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
    git clone https://github.com/<tu-usuario>/EDA_Airbnb.git
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