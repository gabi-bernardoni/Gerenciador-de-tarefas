import tkinter as tk
import mysql.connector

class GerenciadorTarefasApp:
    def __init__(self, root, conn):
        self.root = root
        self.root.title("Gerenciador de Tarefas")
        self.conn = conn
        
        self.root.configure(bg="#FFFFE0")

        #  Campos projeto 
        
        self.label_nome_projeto = tk.Label(root, text="Nome do Projeto:", bg="#FFFFE0")
        self.label_nome_projeto.pack()
        
        self.nome_projeto = tk.Entry(root)
        self.nome_projeto.pack()
        
        self.label_descricao_projeto = tk.Label(root, text="Descrição do Projeto:", bg="#FFFFE0")
        self.label_descricao_projeto.pack()
        
        self.descricao_projeto = tk.Entry(root)
        self.descricao_projeto.pack()
        
        self.botao_criar_projeto = tk.Button(root, text="Criar Projeto", command=self.criar_projeto, bg="#E0FFFF")
        self.botao_criar_projeto.pack()

        self.botao_deletar_projeto = tk.Button(root, text="Deletar Projeto", command=self.deletar_projeto, bg="#E0FFFF")
        self.botao_deletar_projeto.pack()
        
        # Campos tarefa
        
        self.label_nome_tarefa = tk.Label(root, text="Nome da Tarefa:", bg="#FFFFE0")
        self.label_nome_tarefa.pack()
        
        self.nome_tarefa = tk.Entry(root)
        self.nome_tarefa.pack()
        
        self.label_descricao_tarefa = tk.Label(root, text="Descrição da Tarefa:", bg="#FFFFE0")
        self.label_descricao_tarefa.pack()
        
        self.descricao_tarefa = tk.Entry(root)
        self.descricao_tarefa.pack()
        
        self.label_status_tarefa = tk.Label(root, text="Status da Tarefa:", bg="#FFFFE0")
        self.label_status_tarefa.pack()
        
        self.status_tarefa = tk.Entry(root)
        self.status_tarefa.pack()
        
        self.label_observacoes_tarefa = tk.Label(root, text="Observações da Tarefa:", bg="#FFFFE0")
        self.label_observacoes_tarefa.pack()
        
        self.observacoes_tarefa = tk.Entry(root)
        self.observacoes_tarefa.pack()
        
        self.label_prazo_tarefa = tk.Label(root, text="Prazo da Tarefa:", bg="#FFFFE0")
        self.label_prazo_tarefa.pack()
        
        self.prazo_tarefa = tk.Entry(root)
        self.prazo_tarefa.pack()
        
        self.label_projeto_id = tk.Label(root, text="ID do Projeto:", bg="#FFFFE0")
        self.label_projeto_id.pack()
        
        self.projeto_id = tk.Entry(root)
        self.projeto_id.pack()
        
        self.label_tarefa_id = tk.Label(root, text="ID da Tarefa:", bg="#FFFFE0")
        self.label_tarefa_id.pack()

        self.tarefa_id = tk.Entry(root)
        self.tarefa_id.pack()
        
        self.botao_criar_tarefa = tk.Button(root, text="Criar Tarefa", command=self.criar_tarefa, bg="#E0FFFF")
        self.botao_criar_tarefa.pack()

        self.botao_alterar_tarefa = tk.Button(root, text="Alterar Tarefa", command=self.alterar_tarefa, bg="#E0FFFF")
        self.botao_alterar_tarefa.pack()

        self.botao_deletar_tarefa = tk.Button(root, text="Deletar Tarefa", command=self.deletar_tarefa, bg="#E0FFFF")
        self.botao_deletar_tarefa.pack()
        
        # Resultado consulta
        self.botao_consultar = tk.Button(root, text="Consultar Projetos e Tarefas", command=self.consultar, bg="#E0FFFF")
        self.botao_consultar.pack()
        self.resultado_consulta = tk.Text(root, height=10, bg="#E0FFFF")
        self.resultado_consulta.pack()
        
    def executar_query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()
        
    # PROJETO
    def criar_projeto(self):
        nome_projeto = self.nome_projeto.get()
        descricao_projeto = self.descricao_projeto.get()
        query = f"INSERT INTO projetos (nome, descricao, data_criacao, data_atualizacao) VALUES ('{nome_projeto}', '{descricao_projeto}', NOW(), NOW())"
        self.executar_query(query)
        self.consultar()

    def deletar_projeto(self):
        nome_projeto = self.nome_projeto.get()
        query = f"DELETE FROM projetos WHERE nome = '{nome_projeto}'"
        self.executar_query(query)
        self.nome_projeto.delete(0, tk.END)
        self.consultar()

    # TAREFA
    def criar_tarefa(self):
        nome_tarefa = self.nome_tarefa.get()
        descricao_tarefa = self.descricao_tarefa.get()
        status_tarefa = self.status_tarefa.get()
        observacoes_tarefa = self.observacoes_tarefa.get()
        prazo_tarefa = self.prazo_tarefa.get()
        projeto_id = self.projeto_id.get()
        query = f"INSERT INTO tarefas (nome, descricao, status, observacoes, prazo, data_criacao, data_atualizacao, projeto_id) VALUES ('{nome_tarefa}', '{descricao_tarefa}', '{status_tarefa}', '{observacoes_tarefa}', '{prazo_tarefa}', NOW(), NOW(), {projeto_id})"
        self.executar_query(query)
        self.consultar()

    def alterar_tarefa(self):
        tarefa_id = self.tarefa_id.get()
        nome_tarefa = self.nome_tarefa.get()
        descricao_tarefa = self.descricao_tarefa.get()
        status_tarefa = self.status_tarefa.get()
        observacoes_tarefa = self.observacoes_tarefa.get()
        prazo_tarefa = self.prazo_tarefa.get()
        
        query = f"UPDATE tarefas SET nome = '{nome_tarefa}', descricao = '{descricao_tarefa}', status = '{status_tarefa}', observacoes = '{observacoes_tarefa}', prazo = '{prazo_tarefa}', data_atualizacao = NOW() WHERE id = {tarefa_id}"
        self.executar_query(query)
        self.tarefa_id.delete(0, tk.END)
        self.nome_tarefa.delete(0, tk.END)
        self.descricao_tarefa.delete(0, tk.END)
        self.status_tarefa.delete(0, tk.END)
        self.observacoes_tarefa.delete(0, tk.END)
        self.prazo_tarefa.delete(0, tk.END)
        self.consultar()
       
    def deletar_tarefa(self):
        nome_tarefa = self.nome_tarefa.get()
        query = f"DELETE FROM tarefas WHERE nome = '{nome_tarefa}'"
        self.executar_query(query)
        self.nome_tarefa.delete(0, tk.END)
        self.consultar()

    #CONSULTA
    def consultar(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM projetos"
        cursor.execute(query)
        projetos = cursor.fetchall()

        query = "SELECT * FROM tarefas"
        cursor.execute(query)
        tarefas = cursor.fetchall()

        self.resultado_consulta.delete("1.0", tk.END)
        
        self.resultado_consulta.insert(tk.END, "Projetos:\n")
        for projeto in projetos:
          self.resultado_consulta.insert(tk.END, f"ID: {projeto[0]}, Nome: {projeto[1]}, Descrição: {projeto[2]}, Data de Criação: {projeto[3]}, Data de Atualização: {projeto[4]}\n")

        self.resultado_consulta.insert(tk.END, "\nTarefas:\n")
        for tarefas in tarefas:
          self.resultado_consulta.insert(tk.END, f"ID: {tarefas[0]}, Nome: {tarefas[1]}, Descrição: {tarefas[2]}, Status: {tarefas[3]}, Observações: {tarefas[4]}, Prazo: {tarefas[5]}, Data de Criação: {tarefas[6]}, Data de Atualização: {tarefas[7]}, Projeto ID: {tarefas[8]}\n")

root = tk.Tk()

# Conecção MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="gerenciador_tarefasp"
)

app = GerenciadorTarefasApp(root, conn)
root.mainloop()


conn.close()