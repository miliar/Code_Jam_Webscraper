# abrir arquivo e ler suas linhas
arquivo = open("entrada.txt", "r")
linhas = arquivo.readlines();
arquivo.close()

# inicializar variáveis necessárias
quantidade_casos = int(linhas[0].split()[0])
caso_atual = 1
resultado = []

for contador in range(1, len(linhas)):
    # sair após analisados todos os casos
    if quantidade_casos < caso_atual: break
    
    # ignorar espaços em branco excessivos
    lista = linhas[contador].split()
    
    # ignorar linhas vazias
    if lista == []: continue
    
    # determinar quantidade de botões a apertar
    quantidade_botoes = int(lista[0])
    
    # determinar botões dos robôs, separadamente - tupla (ordem, botão)
    botoes_laranja = []
    botoes_azul = []
    ordem = 1
    
    for contador in range(1, (quantidade_botoes * 2) + 1, 2):
        if lista[contador] == "O": botoes_laranja.append((ordem, int(lista[contador + 1])))
        else: botoes_azul.append((ordem, int(lista[contador + 1])))
        ordem = ordem + 1
    
    # inicializar tempo e posição dos robôs
    tempo = 0
    posicao_laranja = 1
    posicao_azul = 1
    ordem_atual = 1
    
    # enquanto as duas listas não forem vazias
    while botoes_laranja != [] or botoes_azul != []:
        # determinar de quem é o próximo passo
        if botoes_laranja != [] and botoes_laranja[0][0] == ordem_atual:
            # apertar botão caso posição do botão seja igual à atual
            if botoes_laranja[0][1] == posicao_laranja:
                botoes_laranja[0:1] = []
                ordem_atual = ordem_atual + 1
            # mover para direita caso posição do botão seja maior que a atual
            elif botoes_laranja[0][1] > posicao_laranja:
                posicao_laranja = posicao_laranja + 1
            # mover para esquerda caso posição do botão seja menor que a atual
            else:
                posicao_laranja = posicao_laranja - 1
            # verificar se robô azul pode executar alguma ação, e executá-la
            if botoes_azul != [] and botoes_azul[0][1] != posicao_azul:
                if botoes_azul[0][1] > posicao_azul:
                    posicao_azul = posicao_azul + 1
                else:
                    posicao_azul = posicao_azul - 1
        elif botoes_azul != [] and botoes_azul[0][0] == ordem_atual:
            # apertar botão caso posição do botão seja igual à atual
            if botoes_azul[0][1] == posicao_azul:
                botoes_azul[0:1] = []
                ordem_atual = ordem_atual + 1
            # mover para direita caso posição do botão seja maior que a atual
            elif botoes_azul[0][1] > posicao_azul:
                posicao_azul = posicao_azul + 1
            # mover para esquerda caso posição do botão seja menor que a atual
            else:
                posicao_azul = posicao_azul - 1
            # verificar se robô laranja pode executar alguma ação, e executá-la
            if botoes_laranja != [] and botoes_laranja[0][1] != posicao_laranja:
                if botoes_laranja[0][1] > posicao_laranja:
                    posicao_laranja = posicao_laranja + 1
                else:
                    posicao_laranja = posicao_laranja - 1
        # aumentar o tempo e a ordem
        tempo = tempo + 1
    
    # adicionar ao resultado
    resultado.append("Case #" + str(caso_atual) + ": " + str(tempo) + "\n")
    
    # passar para próximo caso
    caso_atual = caso_atual + 1

# gravar arquivo de saída
arquivo = open("saida.txt", "w")
arquivo.writelines(resultado)
arquivo.close()
