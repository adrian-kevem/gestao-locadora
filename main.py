import os
import pickle

VEICULOS_DISPONIVEIS = []
VEICULOS_ALUGADOS = []

def carregar_dados():
    global VEICULOS_DISPONIVEIS, VEICULOS_ALUGADOS
    try:
        if not VEICULOS_DISPONIVEIS:
            with open("database1.db", "rb") as arquivo:
                VEICULOS_DISPONIVEIS = pickle.load(arquivo)
            print("Dados de veículos disponíveis carregados com sucesso!")
        else:
            print("Dados de veículos disponíveis não carregados devido ao 'hardcoded'!")
        if not VEICULOS_ALUGADOS:
            with open("database2.db", "rb") as arquivo:
                VEICULOS_ALUGADOS = pickle.load(arquivo)
            print("Dados de veículos alugados carregados com sucesso!")
        else:
            print("Dados de veículos alugados não carregados devido ao 'hardcoded'!")
    except Exception as error:
        print("Erro ao carregar os dados!")
        print(error)

def salvar_dados():
    global VEICULOS_DISPONIVEIS, VEICULOS_ALUGADOS
    try:
        with open("database1.db", "wb") as arquivo:
            pickle.dump(VEICULOS_DISPONIVEIS, arquivo)
        print("Dados de veículos disponíveis salvos com sucesso!")
        with open("database2.db", "wb") as arquivo:
            pickle.dump(VEICULOS_ALUGADOS, arquivo)
        print("Dados de veículos alugados salvos com sucesso!")
    except Exception as error:
        print("Erro ao salvar os dados!")
        print(error)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    print("====================")
    print("LOCADORA DE VEÍCULOS")
    print("====================")
    print("0 - Sair")
    print("1 - Alugar um veículo")
    print("2 - Exibir veículos alugados")
    print("3 - Devolver um veículo")
    opcao1 = input(">>>>> Escolha uma opção: ")
    return opcao1

def alugar_veiculo():
    limpar_tela()
    print("==============")
    print("ALUGAR VEÍCULO")
    print("==============")
    if VEICULOS_DISPONIVEIS:
        for indice, veiculo in enumerate(VEICULOS_DISPONIVEIS, start=1):
            print(f"{indice} - {veiculo[0]} (R$ {veiculo[1]})")
        try:
            opcao2 = int(input(">>>>> Escolha um veículo: "))
            if 1 <= opcao2 <= len(VEICULOS_DISPONIVEIS):
                dias_aluguel = int(input(">>>>> O veículo será alugado por quantos dias? "))
                print(f"O custo total do aluguel será de R$ {VEICULOS_DISPONIVEIS[opcao2 - 1][1] * dias_aluguel}.")
                opcao3 = input(f">>>>> Deseja confirmar a locação do {VEICULOS_DISPONIVEIS[opcao2 - 1][0]} (1 - SIM / 2 - NÃO): ")
                while opcao3 not in {"1", "2"}:
                    print("Opção inválida!")
                    opcao3 = input(f">>>>> Deseja confirmar a locação do {VEICULOS_DISPONIVEIS[opcao2 - 1][0]} (1 - SIM / 2 - NÃO): ")
                if opcao3 == "1":
                    VEICULOS_ALUGADOS.append(VEICULOS_DISPONIVEIS.pop(opcao2 - 1))
                    print("Veículo alugado e pronto para a retirada!")
            else:
                print("Opção inexistente!")
        except (ValueError, IndexError):
            print("Opção inválida!")
    else:
        print("Não existem veículos disponíveis para aluguel!")
    input("Tecle 'Enter' para continuar...")

def exibir_veiculos_alugados():
    limpar_tela()
    print("=================")
    print("VEÍCULOS ALUGADOS")
    print("=================")
    if VEICULOS_ALUGADOS:
        for indice, veiculo in enumerate(VEICULOS_ALUGADOS, start=1):
            print(f"{indice} - {veiculo[0]}")
    else:
        print("Não existem veículos alugados no momento!")
    input("Tecle 'Enter' para continuar...")

def devolver_veiculo():
    limpar_tela()
    print("=================")
    print("VEÍCULOS ALUGADOS")
    print("=================")
    if VEICULOS_ALUGADOS:
        for indice, veiculo in enumerate(VEICULOS_ALUGADOS, start=1):
            print(f"{indice} - {veiculo[0]}")
        try:
            opcao2 = int(input(">>>>> Escolha um veículo: "))
            if 1 <= opcao2 <= len(VEICULOS_ALUGADOS):
                opcao3 = input(f">>>>> Deseja confirmar a devolução do {VEICULOS_ALUGADOS[opcao2 - 1][0]} (1 - SIM / 2 - NÃO): ")
                while opcao3 not in {"1", "2"}:
                    print("Opção inválida!")
                    opcao3 = input(f">>>>> Deseja confirmar a devolução do {VEICULOS_ALUGADOS[opcao2 - 1][0]} (1 - SIM / 2 - NÃO): ")
                if opcao3 == "1":
                    VEICULOS_DISPONIVEIS.append(VEICULOS_ALUGADOS.pop(opcao2 - 1))
            else:
                print("Opção inexistente!")
        except (ValueError, IndexError):
            print("Opção inválida!")
    else:
        print("Não existem veículos alugados no momento!")
    input("Tecle 'Enter' para continuar...")

if __name__ == "__main__":
    while True:
        limpar_tela()
        carregar_dados()
        opcao1 = exibir_menu()
        while opcao1 not in {"0", "1", "2", "3"}:
            print("Opção inválida!")
            opcao1 = exibir_menu()
        if opcao1 == "0":
            print("Saindo...")
            break
        elif opcao1 == "1":
            alugar_veiculo()
        elif opcao1 == "2":
            exibir_veiculos_alugados()
        elif opcao1 == "3":
            devolver_veiculo()
        salvar_dados()