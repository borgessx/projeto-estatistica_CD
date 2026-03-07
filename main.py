# Projeto Colaborativo - Ciencia de Dados
dados_sujos = [10 , " erro ", 20 , 30 , 40 , None , 50 , 15 , " falha ", 25]
def limpar_dados(dados):
        for item in dados[:]: 
            if (type(item) is str) or item == None:
                dados.remove(item)
        return dados
def calcular_media():
    pass

def calcular_mediana(list):
    valor = (len(list)%2)
    list.sort()
    if valor == 0:
        pos1 = int(((len(list)/2)-1))
        pos2 = int((pos1 + 1))
        mediana = (list[pos1]+list[pos2])/2
    else:
        pos3 = int(((len(list)+1)/2)-1)
        mediana = list[pos3]
    return mediana

def calcular_variancia():
    pass
def obter_extremos ():
    pass
dados = limpar_dados ( dados_sujos )
print ( f" Dados processados : { dados }")