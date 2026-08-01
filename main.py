import streamlit as st

# Configuração da página e SEO básico
st.set_page_config(
    page_title="Processamento e Automação de Dados para Pequenas Empresas",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilização minimalista via CSS customizado
st.markdown("""
    <style>
        /* Esconde elementos padrão do Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Ajustes de fonte e espaçamento */
        html, body, [class*="css"] {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            color: #2D3748;
        }
        
        .main-title {
            font-size: 2.2rem;
            font-weight: 700;
            color: #1A202C;
            text-align: center;
            margin-bottom: 0.5rem;
        }
        
        .subtitle {
            font-size: 1.1rem;
            text-align: center;
            color: #4A5568;
            margin-bottom: 2rem;
        }

        .service-card {
            background-color: #F7FAFC;
            padding: 1.5rem;
            border-radius: 8px;
            border-left: 4px solid #3182CE;
            margin-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown("<h1 class='main-title'>Soluções Inteligentes de Processamento de Dados</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Transformamos dados brutos em decisões eficientes e processos automatizados para a sua empresa.</p>", unsafe_allow_html=True)

st.divider()

# --- SOBRE / SEÇÃO VISUAL 1 ---
col1, col2 = st.columns([1, 1], gap="medium")

with col1:
    st.subheader("Otimize seu tempo e reduza custos")
    st.write("""
    Sua empresa perde horas preenchendo planilhas manuais ou organizando relatórios? 
    
    Desenvolvemos fluxos automatizados de coleta, limpeza e estruturação de dados para que você foque no que realmente importa: **fazer seu negócio crescer**.
    """)

with col2:
    # IMAGEM 1: Recomendado tamanho 800x600 px ou similar (proporção 4:3)
    # Subsitua o link da imagem pelo arquivo local ou URL final do seu serviço
    st.image(
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80",
        caption="Automação e visualização de dados",
        use_container_width=True
    )

st.divider()

# --- SERVIÇOS ---
st.subheader("Nossos Serviços")

st.markdown("""
<div class='service-card'>
    <h4>1. Automação de Coleta e Consolidação</h4>
    <p>Integração de dados vindo de múltiplos sistemas, planilhas, PDFs e APIs em uma única base unificada.</p>
</div>

<div class='service-card'>
    <h4>2. Limpeza e Estruturação de Dados</h4>
    <p>Tratamento de dados incorretos ou duplicados para garantir relatórios confiáveis e sem erros manuais.</p>
</div>

<div class='service-card'>
    <h4>3. Relatórios e Relatórios Gerenciais</h4>
    <p>Criação de painéis simples de ler para acompanhamento diário dos seus principais indicadores (KPIs).</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- SEÇÃO VISUAL 2 E DIFERENCIAIS ---
col3, col4 = st.columns([1, 1], gap="medium")

with col3:
    # IMAGEM 2: Recomendado tamanho 800x600 px ou similar (proporção 4:3)
    st.image(
        "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
        caption="Fluxos de trabalho integrados",
        use_container_width=True
    )

with col4:
    st.subheader("Por que automatizar conosco?")
    st.markdown("""
    * **Implementação rápida:** Sem complicação ou sistemas pesados.
    * **Sob medida:** Soluções desenhadas para a realidade de pequenas empresas.
    * **Segurança:** Tratamento sigiloso e seguro das informações da sua empresa.
    """)

st.divider()

# --- CONTATO E CHAMADA PARA AÇÃO ---
st.subheader("Entre em Contato")
st.write("Fale conosco para entender como podemos automatizar o processamento de dados na sua empresa.")

col_contato, col_vazia = st.columns([2, 1])

with col_contato:
    st.markdown("""
    📧 **E-mail:** contato@suaempresa.com.br  
    📱 **WhatsApp:** (00) 99999-9999  
    📍 **Atendimento:** Presencial na região / Remoto para todo o Brasil
    """)
    
    # Botão com link direto para o WhatsApp
    st.link_button("Falar no WhatsApp Agora", "https://wa.me/5500999999999", type="primary")