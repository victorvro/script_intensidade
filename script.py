import pandas as pd
import re

def verificarmg(descricoes):
    for descricao in descricoes:
        mg = re.search("\d*.\d*MG", descricao)
        if mg is not None:
            return mg.group(0)
    return False
            
def verificarporc(descricoes):
    for descricao in descricoes:
        porc = re.search("\d*.\d*%", descricao)
        if porc is not None: 
            return porc.group(0)
    return False


produtos = pd.read_csv("produtos.csv")
intensidade = []

for i in produtos.itertuples():
    descricoes = i.descreduzida.split()
    porc = verificarporc(descricoes)
    mg = verificarmg(descricoes)
    if porc and mg :
        aux = porc + " " + mg
        intensidade.append(aux)
    elif mg:
        intensidade.append(mg)
    elif porc:
        intensidade.append(porc)
    else:
        intensidade.append('')
        

produtos.insert( 2, "intensidade", intensidade)
produtos.to_csv('teste.csv',index=False)