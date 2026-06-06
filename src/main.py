import json
import requests
import streamlit as st

# ========== CONFIGURAÇÕES ==========
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama3"

# ========== CARREGAR DADOS ==========
# Lendo arquivos diretamente como JSON (ajustado para a sua estrutura)
with open('../data/dados_usuario.json', 'r', encoding='utf-8') as f:
    dados_usuario = json.load(f)

with open('../data/historico_conversas.json', 'r', encoding='utf-8') as f:
    historico_conversas = json.load(f)

# ========== MONTAR CONTEXTO ==========
# Convertendo o histórico JSON para string para o LLM ler
historico_str = json.dumps(historico_conversas, indent=2, ensure_ascii=False)

contexto = f"""
CLIENTE: {dados_usuario.get('nome', 'Usuário')}
OBJETIVO: {dados_usuario.get('objetivo_principal', 'Não definido')}
PATRIMÔNIO: R$ {dados_usuario.get('patrimonio_total', 0)}

ATENDIMENTOS ANTERIORES:
{historico_str}
"""

# ========== SYSTEM PROMPT ==========
SYSTEM_PROMPT = """Você é o CrediIA, um assistente virtual de controle financeiro pessoal.
OBJETIVO: Processar mensagens de gastos, identificar o valor e o cartão mencionado, e atualizar o saldo da fatura com base no contexto fornecido.

REGRAS:
- PRIVACIDADE TOTAL: Nunca armazene dados sensíveis como CPF ou senhas.
- ANTI-ALUCINAÇÃO: Baseie-se estritamente nos dados fornecidos no [CONTEXTO].
- FOCO NO ESCOPO: Recuse educadamente assuntos fora de finanças.
- LINGUAGEM: Responda de forma sucinta e direta, com no máximo 3 parágrafos.
"""


# ========== FUNÇÃO OLLAMA (VIA REQUESTS) ==========
def perguntar(msg):
    prompt = f"{SYSTEM_PROMPT}\n\nCONTEXTO DO CLIENTE:\n{contexto}\n\nPergunta: {msg}"

    payload = {
        "model": MODELO,
        "prompt": prompt,
        "stream": False
    }

    r = requests.post(OLLAMA_URL, json=payload)
    return r.json()['response']


# ========== INTERFACE (STREAMLIT) ==========
st.title("💸 CrediIA, Seu Assistente Financeiro")

# Exibe o input do chat
if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    # Exibe a mensagem do usuário
    st.chat_message("user").write(pergunta)

    # Processa a resposta
    with st.spinner("O CrediIA está pensando..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)