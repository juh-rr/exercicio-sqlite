import sqlite3

conexao = sqlite3.connect('novobanco')
cursor = conexao.cursor()

#1 Criar tabela "aluno" com os campos: id int, nome varchar, idade int, curso varchar
#cursor.execute('CREATE TABLE aluno(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, curso VARCHAR (100))')

#2 Inserir ao menos 5 registros
'''cursor.execute('INSERT INTO aluno (id, nome, idade, curso) VALUES (1, "Fernanda", 18, "Eng. de Sistemas")')
cursor.execute('INSERT INTO aluno (id, nome, idade, curso) VALUES (2, "Marcela", 17, "Administração")')
cursor.execute('INSERT INTO aluno (id, nome, idade, curso) VALUES (3, "Joyce", 20, "Física")')
cursor.execute('INSERT INTO aluno (id, nome, idade, curso) VALUES (4, "Camila", 23, "Biologia")')
cursor.execute('INSERT INTO aluno (id, nome, idade, curso) VALUES (5, "Cristiane", 19, "Pedagogia")')
cursor.execute('INSERT INTO aluno (id, nome, idade, curso) VALUES (6, "Monique", 24, "Eng. Mecânica")')'''

#3 Consultas: todos os registros, nome e idade alunas com >20, todos alunos de engenharia, contar número total de alunos
#dados = cursor.execute('SELECT * FROM aluno')
#dados = cursor.execute('SELECT nome, idade FROM aluno WHERE idade > 20')
#dados = cursor.execute('SELECT * FROM aluno WHERE curso LIKE "Eng%"')
#dados = cursor.execute('SELECT COUNT(*) FROM aluno')



'''for usuario in dados:
    print(usuario)'''

#4 Atualizar idade de um aluna, remover uma aluna
#cursor.execute('UPDATE aluno SET idade=22 WHERE id=4')
    
#5 Criar tabela e inserir dados
#cursor.execute('CREATE TABLE cliente(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)') 
#cursor.execute('INSERT INTO cliente(id, nome, idade, saldo) VALUES (1, "Alessandra", 30, 950.00)')
#cursor.execute('INSERT INTO cliente(id, nome, idade, saldo) VALUES (2, "Rebecca", 60, 4000.00)')
#cursor.execute('INSERT INTO cliente(id, nome, idade, saldo) VALUES (3, "Monique", 24, 1100.00)')

#6 nome e idade > 30, saldo medio, cliente com saldo máximo, clientes com saldo acima de 1000

#dados = cursor.execute("SELECT nome, idade FROM cliente WHERE idade>30")

#dados = cursor.execute('SELECT MAX(saldo) FROM cliente ')
#dados = cursor.execute('SELECT * FROM cliente WHERE saldo > 1000')

#7 Atualizar saldo de cliente, remover cliente pelo ID
#dados.execute('UPDATE cliente set saldo=1500.00 WHERE id=3')
#dados.execute('DELETE FROM cliente WHERE id=1')

#8 Criar tabela comprar, ligar com cliente pelo FK, gerar consultas
#cursor.execute('CREATE TABLE compra(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor FLOAT, FOREIGN KEY (cliente_id) REFERENCES cliente(id))')
#cursor.execute('INSERT INTO compra(id, cliente_id, produto, valor) VALUES (1, 2, "Carregador USB-C", 50.00)')
#cursor.execute('INSERT INTO compra(id, cliente_id, produto, valor) VALUES (2, 3, "Airpods", 300.00)')
#cursor.execute('INSERT INTO compra(id, cliente_id, produto, valor) VALUES (3, 2, "Película Motorola", 60.00)')

dados = cursor.execute('SELECT cl.nome, co.produto, co.valor FROM cliente cl INNER JOIN compra co WHERE cl.id = co.cliente_id ORDER BY cl.nome')

for usuario in dados:
    print(usuario)

conexao.commit()
conexao.close()