# Projeto Colaborativo - Ciencia de Dados
dados_sujos = [10 , " erro ", 20 , 30 , 40 , None , 50 , 15 , " falha ", 25]
def limpar_dados(dados):
        for item in dados[:]: 
            if (type(item) is str) or item == None:
                dados.remove(item)
        return dados
def calcular_media():
    pass

def calcular_media (dados) :
    return sum(dados) / len(dados)
  
def calcular_mediana () :
    pass

def calcular_variancia () :
    pass
def obter_extremos (dados) :

    extremo_maior = max(dados)
    extremo_menor = min(dados)
    extremos = [extremo_maior, extremo_menor]
    return extremos

dados = limpar_dados ( dados_sujos )
print ( f" Dados processados : { dados }")

print(f"Verificado por Tayllor Beatriz Queiroz Costa")
print(f"verificado por nicolas")
print(f"Verificado por Vítor Domingos")

