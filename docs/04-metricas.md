# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação de um agente de IA deve ser um processo contínuo e pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define um conjunto fixo de perguntas e valida as respostas esperadas;
2. **Feedback real:** Pessoas testam o agente em cenários variados e atribuem notas de desempenho.

---

## Métricas de Qualidade

Utilize esta tabela para guiar a análise dos resultados durante os testes:

| Métrica | O que avalia | Exemplo de teste |
|---------|------------|------------------|
| **Assertividade** | O agente registra o gasto exatamente como eu falei? | Lançar um gasto e conferir se o valor e o cartão estão certos. |
| **Segurança** | O agente evitou alucinações (inventar dados)? | Tentar lançar um gasto inexistente e ver se ele avisa o erro. |
| **Coerência** | O agente lembra do que combinamos nesta conversa? | Perguntar "Quais foram os gastos que registrei durante esta conversa?" |

---

## Exemplos de Cenários de Teste

Utilize os roteiros abaixo para validar o comportamento do seu agente e garantir consistência após cada ajuste:

### Teste 1: Resumo dos gastos informados
* **Pergunta:** "Quais foram os gastos que registrei durante esta conversa?"
* **Resposta esperada:** O agente deve listar exatamente os itens que foram informados nesta sessão e confirmar o valor total.
* **Resultado:** [ ] Correto  [x] Incorreto

### Teste 2: Registro de gastos
* **Pergunta:** "Salve um gasto de R$ 150,00 no cartão de crédito em 'Supermercado' no dia de hoje."
* **Resposta esperada:** O agente confirma que o lançamento foi registrado corretamente na base de dados ou no arquivo de transações com a categoria e data corretas.
* **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
* **Pergunta:** "Pode me indicar uma receita de bolo para o fim de semana?"
* **Resposta esperada:** O agente declina o pedido, reafirmando seu propósito exclusivo de consultoria e registro financeiro.
* **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
* **Pergunta:** "Por que a ação da empresa X caiu tanto hoje?"
* **Resposta esperada:** O agente admite que não possui acesso a dados de mercado em tempo real ou informações sobre a empresa X, evitando especulações.
* **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões. Use este espaço para documentar a evolução:

**O que funcionou bem:**
- **Processamento de intenção:** O agente identificou corretamente o valor (R$ 150,00), o cartão (Inter) e a ação de salvar.
- **Atualização lógica:** O sistema executou o cálculo de saldo e manteve o histórico de atendimentos atualizado na estrutura de dados.
- **Robustez nos limites (Testes 3 e 4):** O agente demonstrou alta capacidade de respeitar as diretrizes de escopo, recusando com eficácia temas alheios às finanças.

**O que pode melhorar (Ajustes de prompt/lógica):**
- **Ocultar dados técnicos:** O agente está mostrando textos técnicos (os códigos JSON) na tela do chat. Isso deve ficar escondido, aparecendo apenas para você nos bastidores.
- **Melhorar a explicação do saldo:** O valor aparece como negativo (R$ -150,00), o que pode confundir. O ideal é que ele informe algo como "Gasto registrado com sucesso. Fatura atual: R$ 150,00".
- - **Persistência de histórico:** O agente não mantém os gastos registrados entre interações; cada nova entrada sobrescreve o estado anterior. Isso impede consultas posteriores e compromete a coerência.  
- **Clareza na estrutura de saída:** A forma como os dados são exibidos (bloco JSON) não é amigável para o usuário final. É necessário apresentar o resumo dos gastos em linguagem natural, deixando os dados técnicos apenas para uso interno.  