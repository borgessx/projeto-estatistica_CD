# Projeto Colaborativo - Ciencia de Dados
dados_sujos = [10 , " erro ", 20 , 30 , 40 , None , 50 , 15 , " falha ", 25]
def limpar_dados(dados):
        for item in dados[:]: 
            if (type(item) is str) or item == None:
                dados.remove(item)
        return dados
def calcular_media():
    pass
def calcular_mediana():
    pass
def calcular_variancia():
    pass
def obter_extremos ():
    pass
dados = limpar_dados ( dados_sujos )
print ( f" Dados processados : { dados }")
print('Verificado por Tayllor Beatriz Queiroz Costa')