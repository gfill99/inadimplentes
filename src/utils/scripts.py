import duckdb

def create_database():
    sql_script = """
    -- Criando as tabelas do projeto de análise de crédito

    CREATE TABLE IF NOT EXISTS Clientes (
        id_cliente INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        renda_mensal FLOAT NOT NULL,
        score_credito INTEGER NOT NULL,
        cidade TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Emprestimos (
        id_emprestimo INTEGER PRIMARY KEY,
        id_cliente INTEGER REFERENCES Clientes(id_cliente),
        valor_emprestado FLOAT NOT NULL,
        taxa_juros FLOAT NOT NULL,
        parcelas INTEGER NOT NULL,
        data_concessao DATE NOT NULL,
        status TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Pagamentos (
        id_pagamento INTEGER PRIMARY KEY,
        id_emprestimo INTEGER REFERENCES Emprestimos(id_emprestimo),
        data_pagamento DATE NOT NULL,
        valor_pago FLOAT NOT NULL,
        atrasado BOOLEAN NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Inadimplencia (
        id_cliente INTEGER REFERENCES Clientes(id_cliente),
        total_em_atraso FLOAT NOT NULL,
        dias_atraso INTEGER NOT NULL,
        percentual_divida_sobre_renda FLOAT NOT NULL
    );
    """

    print("Esquemas e tabelas criados com sucesso!")
    return sql_script

#Função que recebe um INSERT de uma tabela criada
def ler_query(query_name):
    with open(f'../database/{query_name}.sql', "r", encoding="utf-8") as file:
        sql_text = file.read()
        return sql_text
    
    