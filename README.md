# Análise de Crédito e Inadimplência

Este projeto visa analisar dados de crédito e inadimplência de clientes de um sistema bancário, com foco em identificar padrões de comportamento de inadimplência, taxas de juros e riscos associados, além de criar uma base de dados para suportar futuras análises financeiras.

# Tecnologias utilizadas:


-	**Python**

-	**Pandas** (para manipulação de dados)

-	**Matplotlib / Seaborn** (para visualização de dados)

-	**DuckDB** (para gerenciamento do banco de dados)

-	**SQL** (para criação e manipulação de tabelas no banco de dados)


# Objetivos:


-	Analisar a inadimplência dos clientes: Identificar as faixas de dívida e os riscos associados.

-	Avaliar a distribuição de clientes por cidade e faixa de dívida.

-	Analisar a média de taxas de juros por faixa de score de crédito.

-	Investigar o perfil de inadimplentes em diferentes cidades e faixas de dívida.


Estrutura do projeto:


- `data/` → Arquivos de dados utilizados nas análises (banco de dados e consultas SQL).

- `notebooks/` → Códigos e gráficos gerados durante a análise.

-	`scripts/` → Funções utilizadas para manipulação de dados e criação de tabelas no banco.

-	`configs.py` → Arquivo de configuração para gerenciamento de caminhos de módulos.

- `main.ipynb` → Arquivo principal que executa o código, realizando as consultas e gerando as visualizações.

# Resultados

A análise revelou várias informações sobre o perfil de inadimplentes, como:

- As cidades com maior número de inadimplentes.
- A correlação entre o score de crédito e as taxas de juros médias.
- A distribuição de clientes por faixa de dívida, com base em seu total de atraso.

