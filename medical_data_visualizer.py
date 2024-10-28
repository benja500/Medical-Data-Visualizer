import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Importar los datos del archivo CSV
df = pd.read_csv('medical_examination.csv')

# 2. Crear la columna 'overweight'
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3. Normalizar los datos (colesterol y glucosa)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Dibujar el gráfico categórico
def draw_cat_plot():
    # Crear un DataFrame para el cat plot usando pd.melt
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Agrupar los datos y formatearlos
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # Dibujar el gráfico categórico usando seaborn.catplot
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', kind='bar', data=df_cat).fig

    # Guardar la imagen y devolver la figura
    fig.savefig('catplot.png')
    return fig

# 5. Dibujar el mapa de calor (Heatmap)
def draw_heat_map():
    # Limpiar los datos según las condiciones dadas
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calcular la matriz de correlación
    corr = df_heat.corr()

    # Generar una máscara para la parte superior del triángulo
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Configurar la figura de matplotlib
    fig, ax = plt.subplots(figsize=(12, 8))

    # Dibujar el mapa de calor usando seaborn.heatmap
    sns.heatmap(corr, annot=True, fmt='.1f', mask=mask, square=True, linewidths=0.5, cbar_kws={'shrink': 0.5}, ax=ax)

    # Guardar la imagen y devolver la figura
    fig.savefig('heatmap.png')
    return fig
