class ContaCorrente():
    def __init__(self, conta, pessoa):
        self.pessoa = pessoa
        self.conta = conta
        self.saldo = 0
        self.limite = 0
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            print('Valor depositado de: ' + str(valor))
        
    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo = self.saldo - valor
                print('Saque do valor de: ' + str(valor))
            else:
                if valor <= self.limite:
                    resposta = input('Deseja sacar do limite? S = SIM e N = Não: ')
                    if resposta == 's' or resposta == 'S':
                        self.limite = self.limite - valor
                        self.saldo = self.saldo - valor
                    elif resposta == 'n' or resposta == 'N':
                        print("O Saldo de sua conta é de = %s" %self.saldo)
                        print("O limite da sua conta é de = %s" %self.limite)
                else:
                    print('O valor que deseja sacar é maior que seu limite atual ' + 
                      'de =  %s' %self.limite)
            
    def alterar_nome(self, nome):
        self.pessoa.nome = nome

    def definir_limite(self, valor):
        if valor > 0:
            self.limite = valor

    def verificar_saldo(self):    
        print("O Saldo de sua conta é de = %s" %self.saldo)
        print("O limite da sua conta é de = %s" %self.limite)
        if self.saldo < 0:
            print("O Saldo Total da sua conta é de = %s" %self.saldo)
        else:
            print("O Saldo Total da sua conta é de = %s" %(self.saldo + self.limite))
    
    def print(self):
        print("Dados: \n" +
              "nome = " + str(self.pessoa.nome) + "\n" +
              "conta corrente = " + str(self.conta) + "\n")



