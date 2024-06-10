import pickle

VEICULOS_DISPONIVEIS = []
VEICULOS_ALUGADOS = []

def carregar_dados():
    global VEICULOS_DISPONIVEIS, VEICULOS_ALUGADOS
    try:
        with open("database1.db", "rb") as arquivo:
            VEICULOS_DISPONIVEIS = pickle.load(arquivo)
        with open("database2.db", "rb") as arquivo:
            VEICULOS_ALUGADOS = pickle.load(arquivo)
        print("Dados carregados com sucesso!")
    except Exception as error:
        print("Erro ao carregar os dados!")
        print(error)

def salvar_dados():
    global VEICULOS_DISPONIVEIS, VEICULOS_ALUGADOS
    try:
        with open("database1.db", "wb") as arquivo:
            pickle.dump(VEICULOS_DISPONIVEIS, arquivo)
        with open("database2.db", "wb") as arquivo:
            pickle.dump(VEICULOS_ALUGADOS, arquivo)
        print("Dados salvos com sucesso!")
    except Exception as error:
        print("Erro ao salvar os dados!")
        print(error)

if __name__ == "__main__":
    carregar_dados()
    print(VEICULOS_DISPONIVEIS)
    print(VEICULOS_ALUGADOS)
    VEICULOS_DISPONIVEIS.append(input("Digite o modelo do veículo disponível: "))
    salvar_dados()