def maximoColuna(matriz, j, valor):
    for linha in matriz:
        if linha[j] > valor:
            return False
    return True

def maximoLinha(matriz, i, valor):
    for elemento in matriz[i]:
        if  elemento > valor:
            return False
    return True

def verificaPosicao(matriz, i, j, resposta):
    if not maximoLinha(matriz, i, matriz[i][j]) and not maximoColuna(matriz, j, matriz[i][j]):
        resposta = "NO"
    return resposta

def eh_possivel(matriz, resposta):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            resposta = verificaPosicao(matriz, i, j, resposta)
            if resposta == "NO":
                return resposta
    return resposta

def resolve_test_case(n):
    linha = raw_input().strip().split(" ")
    N = int(linha[0])
    M = int(linha[1])
    matriz = []
    for i in range(N):
        array = []
        linha = raw_input().strip().split(" ")
        for j in range(M):
            array.append(int(linha[j]))
        matriz.append(array)
    resposta = eh_possivel(matriz, "YES") 
    print "Case #%d:" % (n), resposta

T = input()
for i in range(1, T+1):
    resolve_test_case(i)
