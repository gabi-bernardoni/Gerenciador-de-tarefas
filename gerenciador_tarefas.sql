CREATE DATABASE gerenciador_tarefas;
USE gerenciador_tarefas;

-- Criação da tabela "projetos"
CREATE TABLE projetos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    data_criacao DATETIME NOT NULL,
    data_atualizacao DATETIME NOT NULL
);

-- Criação da tabela "tarefas"
CREATE TABLE tarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    status VARCHAR(50) NOT NULL,
    observacoes TEXT,
    prazo DATE NOT NULL,
    data_criacao DATETIME NOT NULL,
    data_atualizacao DATETIME NOT NULL,
    projeto_id INT,
    FOREIGN KEY (projeto_id) REFERENCES projetos(id)
);