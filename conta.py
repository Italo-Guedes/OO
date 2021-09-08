

class Conta:        #Quando vamos criar o objeto ex: conta = Conta(123,"Nico", 55.5, 1000.0), "conta" não é o objeto e sim a referencia (endereço do objeto), o objeto é "objeto Conta"
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))

        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):      #O "self" é uma referênica que sempre assume o valor da referência que fez a chamada. Ex: conta.extrato(), o self assume o valor de conta
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))


    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino): #Não precisa colocar a conta2(origem), pois já é chamada no método.
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property                   #O @property dispensa o uso do get "def get_limite(self):", ficando "def limite(self):"
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod           #Método estático permite chamar o método sem a criação de um objeto "conta = Conta...", neste caso, é possível saber o nº do banco sem precisar criar conta.
    def codigos_bancos():   #O método estático também pode ser criado nos atributos da Classe, neste caso antes do "__init__", ou seja o atributo faz parte da classe, mas é estático podendo ser chamado sem a craiação do objeto.
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
