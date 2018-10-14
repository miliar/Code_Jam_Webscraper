def encontra_vencedor(matriz):
    saida = "?"
    saida = encontra_solucao_em_colunas(matriz, saida)
    if saida == "X":
        return "X won"
    if saida == "O":
        return "O won"
    saida = encontra_solucao_em_linhas(matriz, saida)
    if saida == "X":
        return "X won"
    if saida == "O":
        return "O won"
    saida = encontra_solucao_em_diagonal_1(matriz, saida)
    if saida == "X":
        return "X won"
    if saida == "O":
        return "O won"
    saida = encontra_solucao_em_diagonal_2(matriz, saida)
    if saida == "X":
        return "X won"
    if saida == "O":
        return "O won"
    if esta_completa(matriz):
        return "Draw"
    return "Game has not completed"

def encontra_solucao_em_colunas(matriz, saida):
    for j in range(4):
        if (matriz[0][j] == "T" or matriz[0][j] == "X") and (matriz[1][j] == "T" or matriz[1][j] == "X") and (matriz[2][j] == "T" or matriz[2][j] == "X") and (matriz[3][j] == "T" or matriz[3][j] == "X"):
            saida = "X"
            return saida
        elif (matriz[0][j] == "T" or matriz[0][j] == "O") and (matriz[1][j] == "T" or matriz[1][j] == "O") and (matriz[2][j] == "T" or matriz[2][j] == "O") and (matriz[3][j] == "T" or matriz[3][j] == "O"):
            saida = "O"
            return saida

def encontra_solucao_em_linhas(matriz, saida):
    for j in range(4):
        if (matriz[j][0] == "T" or matriz[j][0] == "X") and (matriz[j][1] == "T" or matriz[j][1] == "X") and (matriz[j][2] == "T" or matriz[j][2] == "X") and (matriz[j][3] == "T" or matriz[j][3] == "X"):
            saida = "X"
            return saida
        elif (matriz[j][0] == "T" or matriz[j][0] == "O") and (matriz[j][1] == "T" or matriz[j][1] == "O") and (matriz[j][2] == "T" or matriz[j][2] == "O") and (matriz[j][3] == "T" or matriz[j][3] == "O"):
            saida = "O"
            return saida

def encontra_solucao_em_diagonal_1(matriz, saida):
    if (matriz[0][0] == "T" or matriz[0][0] == "X") and (matriz[1][1] == "T" or matriz[1][1] == "X") and (matriz[2][2] == "T" or matriz[2][2] == "X") and (matriz[3][3] == "T" or matriz[3][3] == "X"):
        saida = "X"
        return saida
    elif (matriz[0][0] == "T" or matriz[0][0] == "O") and (matriz[1][1] == "T" or matriz[1][1] == "O") and (matriz[2][2] == "T" or matriz[2][2] == "O") and (matriz[3][3] == "T" or matriz[3][3] == "O"):
        saida = "O"
        return saida

def encontra_solucao_em_diagonal_2(matriz, saida):
    if (matriz[0][3] == "T" or matriz[0][3] == "X") and (matriz[1][2] == "T" or matriz[1][2] == "X") and (matriz[2][1] == "T" or matriz[2][1] == "X") and (matriz[3][0] == "T" or matriz[3][0] == "X"):
        saida = "X"
        return saida
    elif (matriz[0][3] == "T" or matriz[0][3] == "O") and (matriz[1][2] == "T" or matriz[1][2] == "O") and (matriz[2][1] == "T" or matriz[2][1] == "O") and (matriz[3][0] == "T" or matriz[3][0] == "O"):
        saida = "O"
        return saida

def esta_completa(matriz):
    for i in range(4):
        for j in range(4):
            if matriz[i][j] == ".":
                return False
    return True

T = input()
for i in range(1,T+1):
    matriz = []
    for j in range(4):
        linha = raw_input()
        array = []
        for k in range(4):
            array.append(linha[k])
        matriz.append(array)
    linha_vazia = raw_input()
    vencedor = encontra_vencedor(matriz)
    print "Case #%d:" % (i), vencedor
