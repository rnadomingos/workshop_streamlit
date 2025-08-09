import io
import time
from datetime import datetime

import pandas as pd
import streamlit as st

cabecalho = "Widgets"
st.header(cabecalho)

subcabecalhobotao = "Botão"
st.subheader(subcabecalhobotao)

botao = "Clique aqui"
botao_mensagem = "Botão Clicado"

if st.button(botao):
    st.text(botao_mensagem)

# Checkbox

subcabecalho_checkbox = "Checkbox"
st.subheader(subcabecalho_checkbox)

checkbox_label = "Eu aceito os termos"
selecionado =  st.checkbox("Voce aceita os termos:")

if selecionado:
   st.write("Termo aceito")
else:
    st.write("Termo ainda não aceito")

# Radio

subcabecalho_radio = "Radio"
st.subheader(subcabecalho_radio)

opcao_radio = st.radio("Escolha uma opção", ("Opcao1","Opcao2","Opcao3","Opcao4"))

st.write("Selecionado: ", opcao_radio)


# Selectbox - Exibe um menu suspenso para selecionar uma opção
opcao_selectbox = st.selectbox(
    "Selecione uma opção", ["Opção A", "Opção B", "Opção C"]
)
st.write("Opção selecionada:", opcao_selectbox)  # Exibe a opção selecionada

# Multiselect - Exibe um menu suspenso para selecionar várias opções
opcoes_multiselect = st.multiselect(
    "Selecione múltiplas opções", ["Opção 1", "Opção 2", "Opção 3"]
)
st.write(
    "Opções selecionadas:", opcoes_multiselect
)  # Exibe as opções selecionadas

# Slider - Exibe uma barra deslizante para selecionar um valor
valor_slider = st.slider("Selecione um valor", 0, 100, 50)
st.write("Valor selecionado:", valor_slider)  # Exibe o valor selecionado

# Select Slider - Exibe uma barra deslizante com opções de texto
intervalo_slider = st.select_slider(
    "Selecione um intervalo", options=["a", "b", "c", "d"], value=("b", "c")
)
st.write(
    "Intervalo selecionado:", intervalo_slider
)  # Exibe o intervalo selecionado

# Text Input - Exibe uma caixa de entrada de texto
nome = st.text_input("Digite seu nome")
st.write("Nome digitado:", nome)  # Exibe o texto digitado

# Number Input - Exibe uma caixa de entrada de número
numero = st.number_input("Selecione um número", 0, 100)
st.write("Número selecionado:", numero)  # Exibe o número selecionado

# Text Area - Exibe uma área de texto
texto = st.text_area("Escreva um texto")
st.write("Texto digitado:", texto)  # Exibe o texto digitado

# Date Input - Exibe um seletor de data
data = st.date_input("Selecione uma data", datetime.now())
st.write("Data selecionada:", data)  # Exibe a data selecionada

# Sidebar
st.sidebar.title("Barra Lateral")  # Exibe o título da barra lateral
botao_sidebar = st.sidebar.button("Botão na Barra Lateral")
if botao_sidebar:
    st.sidebar.write(
        "Botão na barra lateral clicado!"
    )  # Mensagem exibida ao clicar no botão da barra lateral


# Carregar CSV
subcabecalho_csv = "Carregar CSV"
st.subheader(subcabecalho_csv)  # Exibe um subcabeçalho
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    # Barra de progresso durante o upload
    progress_bar = st.progress(0)

    # Simulação do progresso de carregamento
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i + 1)

    # Lê o CSV
    csv_data = pd.read_csv(uploaded_file)
    st.write("Dados do CSV:")
    st.dataframe(csv_data)  # Exibe o conteúdo do arquivo CSV

    # Soltar balões após o upload
    st.balloons()

    # Função para converter DataFrame para Parquet
    @st.cache_data
    def convert_df_to_parquet(df):
        output = io.BytesIO()
        df.to_parquet(output, index=False)
        return output.getvalue()

    st.download_button(
        label="Baixar dados como Parquet",
        data=convert_df_to_parquet(csv_data),
        file_name="dados.parquet",
        mime="application/octet-stream",
    )