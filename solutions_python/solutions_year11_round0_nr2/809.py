import string

# abrir arquivo e ler suas linhas
arquivo = open("entrada.txt", "r")
linhas = arquivo.readlines();
arquivo.close()

# inicializar variáveis necessárias
quantidade_casos = int(linhas[0].split()[0])
caso_atual = 1
resultado = []

elementos_base = ["Q", "W", "E", "R", "A", "S", "D", "F"]
elementos_nao_base = list(set(string.ascii_uppercase) - set(elementos_base))

for contador in range(1, len(linhas)):
    # sair após analisados todos os casos
    if quantidade_casos < caso_atual: break
    
    # ignorar espaços em branco excessivos
    lista = linhas[contador].split()
    
    # ignorar linhas vazias
    if lista == []: continue
    
    # obter a quantidade de combinações
    quantidade_combinacoes = int(lista[0])
    
    # obter a lista de combinações - dicionário { "base" + "base" : "não base" }
    combinacoes = {}
    for contador in range(0, quantidade_combinacoes):
        combinacoes[lista[contador + 1][0] + lista[contador + 1][1]] = lista[contador + 1][2]
    
    # obter a quantidade de opostos
    quantidade_opostos = int(lista[len(combinacoes) + 1])
    
    # obter a lista de opostos - lista [ "elemento" + "elemento" ]
    opostos = []
    for contador in range(0, quantidade_opostos):
        opostos.append(lista[len(combinacoes) + contador + 2][0] + lista[len(combinacoes) + contador + 2][1])
    
    # obter a quantidade de invocações
    invocacoes = int(lista[len(combinacoes) + len(opostos) + 2])
    
    # obter a sequência de invocação
    sequencia = lista[len(combinacoes) + len(opostos) + 3]
    
    # lista contendo apenas as combinações, sem o resultado da combinação
    lista_combinacoes = list(combinacoes.keys())
    
    # executar a sequência
    sequencia_final = ""
    for invocacao in range(0, invocacoes):
        if sequencia_final == "":
            sequencia_final = sequencia[invocacao]
        else:
            juncao = sequencia_final[-1] + sequencia[invocacao]
            juncao_inversa = sequencia[invocacao] + sequencia_final[-1]
            # se estiverem na lista de combinações, combinar os elementos
            if juncao in lista_combinacoes:
                sequencia_final = sequencia_final[:-1] + combinacoes[juncao]
            elif juncao_inversa in lista_combinacoes:
                sequencia_final = sequencia_final[:-1] + combinacoes[juncao_inversa]
            else:
                # se estiverem na lista de opostos, remover os elementos
                for contador in range(0, len(sequencia_final)):
                    juncao = sequencia_final[contador] + sequencia[invocacao]
                    juncao_inversa = sequencia[invocacao] + sequencia_final[contador]
                    if juncao in opostos or juncao_inversa in opostos:
                        sequencia_final = ""
                        break
                else:
                    # adicionar primeiro elemento à sequência final
                    sequencia_final = sequencia_final + sequencia[invocacao]
    
    # adicionar ao resultado
    resultado.append("Case #" + str(caso_atual) + ": " + (str(list(sequencia_final))).replace("\'", "") + "\n")
    
    # passar para próximo caso
    caso_atual = caso_atual + 1

# gravar arquivo de saída
arquivo = open("saida.txt", "w")
arquivo.writelines(resultado)
arquivo.close()
