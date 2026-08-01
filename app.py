# procodding

import streamlit as st
import pandas as pd

st.title('Minha web page')

dados = pd.read_csv('dados.csv')
df = pd.DataFrame(dados)
st.write(dados)

st.image('img.avif')
# graficos

st.bar_chart(dados, x = 'vendedor', y = 'vendas')

st.map()