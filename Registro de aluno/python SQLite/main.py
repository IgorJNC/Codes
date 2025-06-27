import sqlite3
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect("estudante.db")
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS estudantes (
                       id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       nome TEXT NOT NULL, 
                       email TEXT NOT NULL,
                       telefone TEXT NOT NULL,
                       sexo TEXT NOT NULL,
                       data_nascimento TEXT NOT NULL,
                       endereco TEXT NOT NULL,
                       série TEXT NOT NULL,
                       picture TEXT NOT NULL)''')
    
    def register_student(self, estudantes):
        self.c.execute("INSERT INTO estudantes (nome, email, telefone, sexo, data_nascimento, endereco, série, picture) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                       (estudantes))
        self.conn.commit()

        # mostrar mensagem de sucesso
        messagebox.showinfo("Sucesso", "Estudante registrado com sucesso!")

    def view_all_students(self):
        self.c.execute("SELECT * FROM estudantes")
        dados = self.c.fetchall()

        return dados

    def search_student(self, id):
        self.c.execute("SELECT * FROM estudantes WHERE id=?", (id,))
        dados = self.c.fetchone()

        return dados

    def update_student(self, novos_valores):
        query = "UPDATE estudantes SET nome=?, email=?, telefone=?, sexo=?, data_nascimento=?, endereco=?, série=?, picture=? WHERE id=?"
        self.c.execute(query, novos_valores)
        self.conn.commit()
        messagebox.showinfo("Sucesso", f"Estudante com Id:{novos_valores[8]} foi atualizado!")

    def delete_student(self, id):
        self.c.execute("DELETE FROM estudantes WHERE id=?", (id,))
        self.conn.commit()
        messagebox.showinfo("Sucesso", f"Estudante com Id:{id} foi deletado!")

# Criando uma instância do sistema de registro
sistema_de_registro = SistemaDeRegistro()

# Informações
# estudante = ("João Silva", "joao@gmail.com", "123456789", "Masculino", "2011-01-01", "Rua A, 123", "9º Ano", "foto.jpg")
# sistema_de_registro.register_student(estudante)

# Visualizar todos os estudantes
# todos_estudantes = sistema_de_registro.view_all_students()

# Buscar estudante por ID
# sistema_de_registro.search_student(1)

# Atualizar estudante
# estudante = ("João Silva", "joao@gmail.com", "444444", "Masculino", "2011-01-01", "Rua A, 123", "9º Ano", "foto.jpg", 1)  # O último valor é o ID do estudante a ser atualizado
# aluno = sistema_de_registro.update_student(estudante)

# Deletar estudante
# sistema_de_registro.delete_student(1)






        
        
