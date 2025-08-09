import io
from datetime import datetime

import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Inicio",
    page_icon="👋",
)

# 1. Titulo e Texto

titulo = "Aula Introdutória ao Streamlit"
st.title(titulo)

cabecalho = "Aprendendo os Pricipais Metodos"
st.header(cabecalho)

# Exibição de Texto
subcabecalho_texto = "Metodos de Exibição de Texto"
st.subheader(subcabecalho_texto)

# Texto Simples
texto_simples = (
  "Streamlit facilita a criação de aplicaões web intereativas com Python"
)
st.text(texto_simples)

texto_markdown = " ### Este é um texto em **markdown**!"
st.markdown(texto_markdown)

# Formula em LaTeX
formula_latex = r"""e^{i\pi} + 1 = 0"""
st.latex(formula_latex)

# Código
codigo_exemplo = "x = 42"
st.code(codigo_exemplo)

# Dataframe
data = {"A": [1,2,3,4], "B": [10,20,30,40]}
df = pd.DataFrame(data)
st.dataframe(df, hide_index=True)

# Exibe o DataFrame usando o método table
st.table(df)  # Exibe o DataFrame como uma tabela estática


#JSON
json_exemplo = {"name": "Streamlit", "type": "Web Framework"}
st.json(json_exemplo)

#CSV como string
csv_exemplo = df.to_csv(index=False)
st.write(csv_exemplo)

# Lista
lista_exemplo = [1,2,3,4,5]
st.write("Lista de números:",lista_exemplo)

# 3. Métricas
subcabecalho_metricas = "Métricas"
st.subheader(subcabecalho_metricas)


# Metricas com delta
a, b, c, d, e= st.columns(5)

temperatura = {"label": "Temperatura", "Value": "70 ºF", "delta": "1.2 ºF"}
with a: 
  st.metric(
    label=temperatura["label"],
    value=temperatura["Value"],
    delta=temperatura["delta"]
  )

with b:
    umidade = {"label": "Umidade", "value": "60%", "delta": "-5%"}
    st.metric(
      label=umidade["label"],
      value=umidade["value"],
      delta=umidade["delta"]
    )

with c:
    vento = {"label": "Velocidade do Vento", "value": "15 km/h", "delta": "1%"}
    st.metric(
      label=vento["label"],
      value=vento["value"],
      delta=vento["delta"]
    )

with d: 
    ruido = {"label": "Nivel de Ruído", "value": "40 db", "delta": "6%"}
    st.metric(
      label=ruido["label"],
      value=ruido["value"],
      delta=ruido["delta"]
    )

pressao = {"label": "Pressão atmosférica", "value": "1013 hPa", "delta": "-5%"}
st.metric(
  label=pressao["label"],
  value=pressao["value"],
  delta=pressao["delta"]
)

subcabecalho_graficos = "Gráficos"
st.subheader(subcabecalho_graficos)

chart_data = pd.DataFrame(np.random.randn(20,3), columns=["a", "b", "c"])
st.line_chart(chart_data)
st.bar_chart(chart_data)
st.area_chart(chart_data)

# Mais exemplos de Gráficos
mais_graficos = "Mais exemplos de Gráficos"

st.subheader(mais_graficos)

# Dados granficos de dispersão

scatter_data = pd.DataFrame(np.random.randn(100,2), columns=["x", "y"])
st.plotly_chart({
    "data": [
        {
            "x": scatter_data["x"],
            "y": scatter_data["y"],
            "type": "scatter",
            "mode": "markers",
        }
    ],
    "layout": {"title": "Gráfico de Dispersão"}
})

# Histograma
hist_data = np.random.randn(1000)
st.plotly_chart(
    {
        "data": [{"x": hist_data, "type": "histogram"}],
        "layout": {"title": "Histograma"},
    }
)  # Exibe um histograma

# 5. Mapas
subcabecalho_mapas = "Mapas"
st.subheader(subcabecalho_mapas)  # Exibe um subcabeçalho

# Cria e exibe um mapa
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)
st.map(map_data)  # Exibe um mapa com pontos aleatórios

# 6. Mídia
subcabecalho_midia = "Mídia"
st.subheader(subcabecalho_midia)  # Exibe um subcabeçalho

# Exibe uma imagem
imagem_url = "https://www.streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png"
imagem_legenda = "Streamlit Logo"
st.image(imagem_url, caption=imagem_legenda)  # Exibe uma imagem com legenda

# Exibe um áudio
audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
st.audio(audio_url)  # Exibe um reprodutor de áudio

# Exibe um vídeo
video_url = "https://www.youtube.com/watch?v=B2iAodr0fOo"
st.video(video_url)  # Exibe um reprodutor de vídeo