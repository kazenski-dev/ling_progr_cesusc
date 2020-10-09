from person import *

class Interface:

    global pessoas = {'nomes': nomes[], 'cpfs': cpfs[], 'emails': emails[], 'atividades': atividades[]}

    def busca_padrao(self):
        while True:
            #busca_usuario = input("\nInsira o nome, cpf ou email da pessoa para realizar a busca detalhada...\n")
            pass

    def listar_pessoa(self):
        pass

    def cadastrar_pessoa(self):
        nome_pessoa = input('Qual é o nome da pessoa?\n')
        cpf_pessoa = input('Qual é o cpf da pessoa?\n')
        email_pessoa = input('Qual é o email da pessoa?\n')
        atividade = 1

        print('\n\nEfetuando novo Cadastro...\n')

        cadastro_novo = Pessoa(nome_pessoa, cpf_pessoa, email_pessoa, atividade)
        pessoas.update(cadastro_novo.nome, cadastro_novo.cpf, cadastro_novo.email, cadastro_novo.atividade)
        print(cadastro_novo)

        self.pessoas.append(Pessoa(nome_pessoa, cpf_pessoa, email_pessoa, atividade))
        print('Pessoa cadastrada com sucesso!')

    def alterar_pessoa(self):
        pass

    def excluir_pessoa(self):
        pass

    def loop(self):
        while True:
            cmd = input('\n1 - Listar cadastros\n2 - Cadastrar pessoa\n3 - Alterar cadastro\n4 - Excluir cadastro')
            if cmd == '1':
                self.listar_pessoa()
            elif cmd == '2':
                self.cadastrar_pessoa()
            elif cmd == '3':
                self.alterar_pessoa()
            elif cmd == '4':
                self.exluir_pessoa()
            else:
                print('Não entendi!')
                continue