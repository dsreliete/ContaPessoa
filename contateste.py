from conta import ContaCorrente
from pessoa import Pessoa

def menu():
    print("")
    print("Selecione uma opção:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Verificar Saldo")
    print("4 - Alterar Pessoa")
    print("5 - Definir Limite")
    print("6 - Visualizar dados da Conta")
    print("0 - Sair")


p = Pessoa('Eliete')
cc = ContaCorrente(121256, p)
op = 6
while (op != 0):
    menu()
    op = int(input("\n"))
    if op == 1:
        valor = int(input('Digite o valor que deseja depositar: '))
        cc.depositar(valor)
    elif op == 2:
        valor = int(input('Digite o valor que deseja sacar: '))
        cc.sacar(valor)
    elif op == 3:
        cc.verificar_saldo()
    elif op == 4:
        nome = (input('Digite o nome que deseja alterar: '))
        cc.alterar_nome(nome)
    elif op == 5:
        valor = int(input('Digite o valor do limite que deseja definir: '))
        cc.definir_limite(valor)
    elif op == 6:      
        cc.print()

print("Obrigada por usar os nossos serviços")

