# Base de Conhecimento: CrediIA

## Fontes de Dados
O agente utiliza os seguintes arquivos localizados na pasta raiz do projeto:

- `dados_usuario.json`: Contém o perfil do usuário, lista de cartões cadastrados e os lançamentos efetuados.
- `historico_conversas.json`: Armazena o log das interações passadas para manter a continuidade do aprendizado/contexto.

## Regras de Negócio
- Se o cartão mencionado não constar em `dados_usuario.json`, o agente deve emitir um aviso e solicitar cadastro.
- Todos os lançamentos devem ser registrados com: descrição, valor e data.