from datetime import datetime
import time

class Biblioteca:
    def __init__(self):
        self.aberto = False
        self.referencia_usuarios = Usuarios()
        self.referencia_livros = Livros()

    def expediente(self):
        self.funcionamento = False
        self.data = datetime.now()
        self.hora = self.data.hour

        if 8 <= self.hora < 21:
            self.funcionamento = True
            self.aberto = self.funcionamento
            print('=-' *20)
            print("\x1b[33mSEJA BEM VINDO(A) À BIBLIOTECA PUBLICA DO ESTADO DE PERNAMBUCO\x1b[0m")
            print('=-' *20)
            referencia.desejo_menu()

        else:
            print("\x1b[31mESTAMOS FORA DO HORARIO DE EXPEDIENTE...\x1b[0m")
            print('HORARIO DE EXPEDIENTE: 08:00 - 17:00')
            print('ATÉ BREVE!')
            quit()

    def desejo_menu(self):
        print('-' *20)
        print('SELECIONE O QUE VOCÊ DESEJA FAZER...')
        print('-' *20)
        print('1. Adicionar um novo usuario')
        print('2. Adicionar um novo livro')
        print('3. Emprestimo de livros')
        print('4. Devolver um livro')
        print('5. Verificar usuario')
        print('6. Encerrar programa')
        print('-' *20)

        while True:
            try:
                self.acesso = int(input('O que você deseja fazer? [ESCOLHA UM NUMERO]'))
                if self.acesso in [1, 2, 3, 4, 5, 6]:
                    break
                else:
                    print("\x1b[31m!ERRO! SELECIONE UMA OPÇÃO ENTRE 1 E 6 !ERRO!\x1b[0m")

            except ValueError:
                print("\x1b[31m!ERRO! SÃO ACEITOS APENAS CARACTERES NUMÉRICOS !ERRO!\x1b[0m")

        if self.acesso == 1:
            self.referencia_usuarios.adicionar_usuario()

        elif self.acesso == 2:
            self.referencia_livros.adicionar_livros()

        elif self.acesso == 3:
            self.referencia_livros.livros_disponiveis()

        elif self.acesso == 4:
            self.referencia_livros.devolucao()

        elif self.acesso == 5:
            self.referencia_usuarios.verificar_usuario()

        elif self.acesso == 6:
            print('Obrigado(a) por utilizar nossos serviços, até breve!')
            quit()


class Livros:
    def __init__(self):
        self.acervo_livros = []

    def adicionar_livros(self):
        nome = input('Qual nome do livro:')
        self.acervo_livros.append((nome))
        time.sleep(1)
        print('Livro adicionado com sucesso...')
        referencia.desejo_menu()

    def livros_disponiveis(self):
        if not self.acervo_livros:
            print('Não temos livros em nosso acervo!')
            referencia.desejo_menu()

        else:
            print(self.acervo_livros)
            print('O que você deseja?')
            print('1. Alugar um livro')
            print('2. Voltar ao MENU')
            while True:
                try:
                    self.add_usuario = int(input('O que você deseja fazer? [ESCOLHA UM NÚMERO]'))
                    if self.add_usuario in [1, 2]:
                        break
                    else:
                        print("\x1b[31m!ERRO! SELECIONE UMA OPÇÃO ENTRE 1 E 2 !ERRO!\x1b[0m")

                except ValueError:
                    print("\x1b[31m!ERRO! SÃO ACEITOS APENAS CARACTERES NUMÉRICOS !ERRO!\x1b[0m")

            if self.add_usuario == 1:
                self.aluguel = input('Qual nome do livro você deseja alugar?')
                self.usuario = input('Qual o seu nome?')
                for elemento in self.acervo_livros:
                    if elemento == self.aluguel:
                        self.acervo_livros.remove(elemento)
                        referencia_usuarios.usuarios.append((self.aluguel, self.usuario))
                        print('Livro alugado com sucesso...')
                        referencia.desejo_menu()
                        break
                else:
                    print('Não temos esse livro disponível no momento!')
                    referencia.desejo_menu()
                    

            if self.add_usuario == 2:
                referencia.desejo_menu()

    def devolucao(self):
        usuario_emprestimo = input('Qual seu nome?')
        for livro_emprestado in referencia_usuarios.usuarios:
            livro, nome = livro_emprestado
            if nome == usuario_emprestimo:
                referencia_usuarios.usuarios.remove(livro_emprestado)
                self.acervo_livros.append(livro)
                time.sleep(1)
                print('Livro devolvido com sucesso...')
                referencia.desejo_menu()
                break
        else:
            print('Você não tem livros emprestados no momento!')
            referencia.desejo_menu()


class Usuarios:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self):
        nome = input('Qual nome do usuário:')
        idade = input('Qual idade do usuário?')
        self.usuarios.append((nome, idade))
        time.sleep(1)
        print('Usuário adicionado com sucesso...')
        self.desejo()

    def verificar_usuario(self):
        usuario_verificar = input('Qual seu nome?')
        for nome, idade in self.usuarios:
            if nome == usuario_verificar:
                print('USUÁRIO ENCONTRADO...')
                time.sleep(1)
                print(f'Nome: {nome}, Idade: {idade}')
                self.desejo()
        else:
            print('Usuário não encontrado!')
            self.desejo()

    def desejo(self):
        print('O que você deseja?')
        print('1. Adicionar outro usuário')
        print('2. Voltar ao MENU')
        while True:
            try:
                self.add_usuario = int(input('O que você deseja fazer? [ESCOLHA UM NÚMERO]'))
                if self.add_usuario in [1, 2]:
                    break
                else:
                    print("\x1b[31m!ERRO! SELECIONE UMA OPÇÃO ENTRE 1 E 2 !ERRO!\x1b[0m")

            except ValueError:
                print("\x1b[31m!ERRO! SÃO ACEITOS APENAS CARACTERES NUMÉRICOS !ERRO!\x1b[0m")

        if self.add_usuario == 1:
            self.adicionar_usuario()

        elif self.add_usuario == 2:
            referencia.desejo_menu()

if __name__ == "__main__":
    referencia = Biblioteca()
    referencia_usuarios = Usuarios()
    referencia.expediente()
