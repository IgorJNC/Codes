import os
import streamlit as st
from groq import Groq 

st.set_page_config(
    page_title="AI Coder",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

CUSTOM_PROMPT = """
Você é o "AI Coder", um assistente de programação especializado em ajudar desenvolvedores a escrever, revisar e depurar código. Você é capaz de entender múltiplas linguagens de programação, incluindo Python, JavaScript, Java, C++, Ruby, e mais. Seu objetivo é fornecer soluções claras e eficientes para problemas de codificação, sugerir melhores práticas e ajudar na otimização do código.

REGRAS DE OPERAÇÃO:
1. **Foco na Programação**: Concentre-se exclusivamente em questões relacionadas à programação e desenvolvimento de software.
2. **Estrutura de Resposta**: Forneça respostas estruturadas com exemplos de código, explicações detalhadas, sugestões de melhorias, documentação de referência (Insira no final da resposta uma seção mostrando a documentação), clareza e precisão.
3. **Linguagens Suportadas**: Esteja preparado para lidar com uma variedade de linguagens de programação e frameworks.
4. **Melhores Práticas**: Sempre sugira melhores práticas de codificação, incluindo segurança, eficiência e legibilidade.
5. **Depuração**: Ajude na identificação e correção de bugs, fornecendo soluções passo a passo.
6. **Atualização Contínua**: Mantenha-se atualizado com as últimas tendências e tecnologias em desenvolvimento de software.
7. **Limitações**: Se a pergunta estiver fora do escopo de programação, informe educadamente que você só pode ajudar com questões relacionadas a desenvolvimento de software.
"""
with st.sidebar:
    st.title("🤖 AI Coder")
    st.markdown("Um assistente de IA focado em ajudar desenvolvedores com suas necessidades de codificação.")
    groq_api_key = st.text_input(
        "Insira sua chave de API Groq",
        type="password",
        help="Obtenha sua chave de API em https://console.groq.com/keys"
        )
    
    st.markdown("---")
    st.markdown("Desenvolvido para ajudar desenvolvedores a escrever, revisar e depurar código de forma eficiente. A IA pode cometer erros, sempre revise o código gerado.")

    st.markdown("---")
    st.markdown("Feito por Igor José - https://github.com/IgorJNC/Codes")

st.title("🤖 AI Coder")

st.title("Uma IA focada em ajudar desenvolvedores com suas necessidades de codificação.")

st.caption("Faça sua pergunta e a IA responderá com código, explicações e sugestões.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

client = None

if groq_api_key:
    try:
        client = Groq(api_key = groq_api_key)
    
    except Exception as e:
        st.sidebar.error(f"Erro ao conectar com a API Groq: {e}")
        st.stop()

elif st.session_state.messages:
    st.warning("Por favor, insira sua chave de API Groq na barra lateral.")

if prompt := st.chat_input("Qual é a sua dúvida? "):

    if not client:
        st.warning("Por favor, insira sua chave de API Groq na barra lateral.")
        st.stop()
    
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    messages_for_api = [{"role": "system", "content": CUSTOM_PROMPT}]
    for message in st.session_state.messages:
        messages_for_api.append(message)

    with st.chat_message("assistant"):

        with st.spinner("Analisando a sua dúvida..."):

            try:

                chat_completion = client.chat.completions.create(
                    messages = messages_for_api,
                    model = "openai/gpt-oss-20b",
                    temperature = 0.7,
                    max_tokens = 2048,
                )

                ai_resposta = chat_completion.choices[0].message.content

                st.markdown(ai_resposta)

                st.session_state.messages.append({"role": "assistant", "content": ai_resposta})

            except Exception as e:
                st.error(f"Ocorreu um erro ao processar sua solicitação: {e}")

st.markdown(
    """
    <div style="text-align: center; color: gray;">
        <hr>
        <p>Feito por Igor José</p>
    <div>
    """,
    unsafe_allow_html=True
)
