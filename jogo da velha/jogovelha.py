from numpy import random


class Jogador:
    def __init__(self) -> None:
        self.nome = input("Qual o seu nome? ")
        self.simbolo = input("Você quer 'X' ou 'O'? ")

    def fazer_jogada(self) -> None:
        # Vazia para ser implementada nas subclasses
        pass


class JogadorHumano(Jogador):
    def fazer_jogada(self) -> int:
        """Marca uma casa do tabuleiro pela escolha do jogador.

        Returns:
            int: Retorna o valor da casa que o jogador quer marcar.
        """
        while True:
            jogada = int(input(f"É a sua vez, {self.nome}. Insira o número da casa que quer marcar: "))
            # Imprime uma mensagem se a casa estiver ocupada (tentar novamente)
            if jogo.tabuleiro.marcar_casa(self.simbolo, jogada) == "Erro":
                print("Você tentou marcar uma casa ocupada, tente novamente.")
                continue
            else:
                break


class JogadorComputador(Jogador):
    # Definida apenas a estratégia 'aleatoria', podendo ser programadas outras
    estrategias = ["aleatoria"]

    def __init__(self, nome: str, estrategia: str) -> None:
        """Define o simbolo e a estrategia do jogador bot

        Args:
            nome (str): O nome dado pelo jogador ao bot
            estrategia (str): A estrategia que o bot irá utilizar para jogar
        """
        # Definindo o simbolo do bot com base na escolha do jogador humano.
        self.simbolo = ""
        if jogador.simbolo == 'X':
            self.simbolo = 'O'
        else:
            self.simbolo = 'X'
        self.nome = nome
        if estrategia in self.estrategias:
            self.estrategia = estrategia

    def fazer_jogada(self) -> None:
        """Método para o jogador bor fazer uma jogada

        Através do módulo numpy 'random.randint', escolhe um número aleatório
        e a casa correspondente a esse número, se estiver vazia, será marcada.
        Se não estiver vazia, tenta novamente até encontrar uma que esteja.
        """
        if self.estrategia == 'aleatoria':
            print("Agora é a vez do bot: ")
            # Verificando se uma casa aleatória está vazia e marcando ela
            while True:
                casa = random.randint(1, 10)
                if jogo.tabuleiro.casas[int(casa) - 1] == "":
                    jogo.tabuleiro.marcar_casa(self.simbolo, casa)
                    break
                elif "" in jogo.tabuleiro.casas:
                    continue
                else:
                    break
        else:
            print(f"A estratégia '{estrategia}' é invalida.")


class Tabuleiro:
    def __init__(self) -> None:
        self.casas = ['', '', '', '', '', '', '', '', '']

    def pegar_tabuleiro(self) -> str:
        # Lista para guardar as sublistas de 3 itens da lista 'self.casas'
        self.lista_casas = []
        for i in range(0, len(self.casas), 3):
            sublista = self.casas[i:i + 3]
            self.lista_casas.append(sublista)
        return self.lista_casas

    def marcar_casa(self, simbolo: str, casa: int) -> str:
        """Marca uma casa escolhida por um jogador

        Args:
            simbolo (str): Símbolo que vai ser marcado na casa escolhida
            casa (int): Número que corresponde a uma das casas do tabuleiro

        Returns:
            str: Retorna o tabuleiro com a casa marcada. Se a casa escolhida
            não estiver em branco, retorna 'Erro' para ser tratado.
        """
        while True:
            if self.casas[int(casa)-1] == '':
                self.casas[int(casa) -1] = simbolo
                jogo.tabuleiro.imprimir_tabuleiro()
                break
            else:
                return "Erro"

    def imprimir_tabuleiro(self) -> str:
        """Imprime o tabuleiro de maneira formatada e não de lista de listas

        Returns:
            str: Retorna strings que são cada linha do tabuleiro.
        """
        lista = jogo.tabuleiro.pegar_tabuleiro()
        for sublista in lista:
            # Imprimindo cada linha de maneira formatada
            texto = f"  {sublista[0]}  |  {sublista[1]}  |  {sublista[2]}  "
            print(texto)
            print("-" * len(texto))
        print("\n")


class JogoVelha:
    def __init__(self, jogadorhumano: Jogador, jogadorbot: Jogador) -> None:
        """A classe 'JogoVelha' é onde vai funcionar o jogo

        Args:
            jogadorhumano (Jogador): É o jogador controlado pelo usuário
            jogadorbot (Jogador): É o jogador computador
        """
        self.jogadores = [jogadorhumano, jogadorbot]
        self.tabuleiro = Tabuleiro()
        self.turno = 0

    def jogador_atual(self) -> Jogador:
        """Verifica qual é o jogador atual com base no turno

        Returns:
            Jogador: Retorna o jogador da vez
        """
        # A vez começa sempre com o jogador humano
        if self.turno % 2 == 0:
            current_player = jogador
            return current_player
        elif self.turno % 2 != 0:
            current_player = jogador_bot
            return current_player

    def checar_fim_de_jogo(self) -> str:
        """Checa as possíveis condições de vitória de um dos jogadores

        Returns:
            str: Retorna uma string 'Fim' se uma condição de vitória for
            atendida
        """
        # Variáveis armazenando algumas casas (máx. de 80 caracteres por linha)
        casa1 = self.tabuleiro.casas[0]
        casa3 = self.tabuleiro.casas[2]
        casa5 = self.tabuleiro.casas[4]
        casa7 = self.tabuleiro.casas[6]
        casa8 = self.tabuleiro.casas[7]
        casa9 = self.tabuleiro.casas[8]
        symbol = self.jogador_atual().simbolo
        if casa1 == symbol:
            # Verificando a vitória na primeira linha
            if self.tabuleiro.casas[1] == symbol and casa3 == symbol:
                print(f"O jogador {self.jogador_atual().nome} venceu.")
                return "Fim"
            # Verificando a vitória na diagonal principal
            elif casa5 == symbol and casa9 == symbol:
                print(f"O jogador {self.jogador_atual().nome} venceu.")
                return "Fim"
            # Verificando a vitória na primeira coluna
            elif self.tabuleiro.casas[3] == symbol and casa7 == symbol:
                print(f"O jogador {self.jogador_atual().nome} venceu.")
                return "Fim"
        if casa3 == symbol:
            # Verificando a vitória na diagonal secundária
            if casa5 == symbol and casa7 == symbol:
                print(f"O jogador {self.jogador_atual().nome} venceu.")
                return "Fim"
            # Verificando a vitória na terceira coluna
            elif self.tabuleiro.casas[5] == symbol and casa9 == symbol:
                print(f"O jogador {self.jogador_atual().nome} venceu.")
                return "Fim"
        if casa8 == symbol:
            # Verificando a vitória na terceira linha
            if self.tabuleiro.casas[6] == symbol and casa9 == symbol:
                print(f"O jogador {self.jogador_atual().nome} venceu.")
                return "Fim"
            # Verificando a vitória na segunda coluna
            elif casa5 == symbol and self.tabuleiro.casas[1] == symbol:
                print(f"O jogador {self.jogador_atual().nome} venceu.")
                return "Fim"
        if self.tabuleiro.casas[5] == symbol:
            # Verificando a vitória na segunda linha
            if self.tabuleiro.casas[3] == symbol and casa5 == symbol:
                print(f"O jogador {self.jogador_atual().nome} venceu.")
                return "Fim"
        # Verifica se todas as casas estão preenchidas, mas não há vitória
        if all(casa != "" for casa in self.tabuleiro.casas):
            print("Deu velha!")

    def jogar(self) -> None:
        """Método jogar para executar o jogo

        Aqui são solicitadas as jogadas aos jogadores. A cada jogada, verifica
        se houve uma vitória, caso contrário, passa para o próximo turno.
        """
        while True:
            self.jogador_atual().fazer_jogada()
            if self.checar_fim_de_jogo() == "Fim":
                break
            else:
                self.turno += 1


# Instanciando os objetos:
jogador = JogadorHumano()
jogador_bot = JogadorComputador(input("Escolha o nome do seu oponente: "), "aleatoria")
jogo = JogoVelha(jogador, jogador_bot)

jogo.tabuleiro.pegar_tabuleiro()
jogo.jogar()
