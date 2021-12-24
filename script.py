import pandas as pd
import re

produtos = pd.read_csv("produtos.csv")
intensidade = []

for i in produtos.itertuples():
    porc = re.search("(\d+\S*\d*%)", i.descreduzida)
    mg = re.search("(\d+\S*\d*MG)", i.descreduzida)
    if porc and mg is not None:
        aux = porc.group(0) + " // " + mg.group(0)
        intensidade.append(aux)
    elif mg:
        intensidade.append(mg.group(0))
    elif porc:
        intensidade.append(porc.group(0))
    else:
        intensidade.append('')
        

produtos.insert( 2, "intensidade", intensidade)
produtos.to_csv("teste.csv",index=False)