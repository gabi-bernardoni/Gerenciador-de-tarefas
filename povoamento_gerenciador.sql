use gerenciador_tarefasp;
INSERT INTO projetos (nome, descricao, data_criacao, data_atualizacao) VALUES ('Arquitetura', 'Reforma Banheiro', '2023-08-13 16:30:00', '2023-08-13 16:30:00' );
INSERT INTO projetos (nome, descricao, data_criacao, data_atualizacao) VALUES ('Montadora BMW', 'X1', '2023-08-13 16:32:00', '2023-08-13 16:32:00' );
INSERT INTO projetos (nome, descricao, data_criacao, data_atualizacao) VALUES ('Reforma Casa', 'Cozinha', '2023-08-13 16:35:15', '2023-08-13 16:35:15' );
INSERT INTO projetos (nome, descricao, data_criacao, data_atualizacao) VALUES ('Carro', 'HB20', '2023-08-13 17:00:00', '2023-08-13 17:00:00' );
INSERT INTO projetos (nome, descricao, data_criacao, data_atualizacao) VALUES ('Arquitetura', 'Reforma Cozinha', '2023-08-13 17:10:25', '2023-08-13 17:10:25' );

use gerenciador_tarefasp;
INSERT INTO tarefas (nome, descricao, status, observacoes, prazo, data_criacao, data_atualizacao, projeto_id) VALUES ('Obra', 'Reforma Banheiro','Em andamento', 'Pintura Teto','2023-10-09', '2023-08-13 17:10:25', '2023-08-13 17:10:25', 8);
INSERT INTO tarefas (nome, descricao, status, observacoes, prazo, data_criacao, data_atualizacao, projeto_id) VALUES ('Montadora', 'Portas BMW','Encerrado', 'Portas Pretas','2023-09-09', '2023-08-13 17:10:25', '2023-08-13 17:10:25', 5);
INSERT INTO tarefas (nome, descricao, status, observacoes, prazo, data_criacao, data_atualizacao, projeto_id) VALUES ('Obra', 'Reforma Cozinha','Em andamento', 'Fiação','2023-09-28', '2023-08-13 17:10:25', '2023-08-13 17:10:25', 8);
INSERT INTO tarefas (nome, descricao, status, observacoes, prazo, data_criacao, data_atualizacao, projeto_id) VALUES ('Manutenção', 'Embreagem','Em andamento', 'Troca','2023-12-01', '2023-08-13 17:10:25', '2023-08-13 17:10:25', 7);
INSERT INTO tarefas (nome, descricao, status, observacoes, prazo, data_criacao, data_atualizacao, projeto_id) VALUES ('Compra', 'Móveis','Em andamento', 'Porcelanato','2023-11-09', '2023-08-13 17:10:25', '2023-08-13 17:10:25', 8);