class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property   #dispensa o uso de "()" para chamar o método
    def nome(self):
        print("Chamando @property nome()")
        return self.__nome.title() #Garante a primeira letra do nome como maiúscula

    @nome.setter
    def nome(self, nome):
        print("Chamando setter nome()")
        self.__nome = nome

