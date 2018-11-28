#!/usr/bin/python3
from sys import argv

script, filename = argv

txt = open(filename)

casos = int(txt.readline())

def incluirPessoa (stalls):
    N = len(stalls)
    if N%2 != 0:
        stalls = '.' * (N/2) + '0' + '.' * (N/2)
    else:
        stalls = '.' * ((N/2)-1) + '0' + '.' * (N/2)
    #print stalls
    return stalls

def longestrun(myList):
    size = 1
    max_size = 0
    for i in range(len(myList)-1):
        if myList[i] == '.':
            if myList[i+1] == myList[i]:
                size += 1
            else: 
                if max_size<size:
                    max_size = size 
                size = 1
        if max_size<size:
            max_size = size                
    return myList.find('.'*max_size), max_size

def shortestrun(myList):
    size = 1
    min_size = len(myList)
    if '.' not in myList:
        return 0
    for i in range(len(myList)-1):
        if myList[i] == '.':
            if myList[i+1] == myList[i]:
                size += 1
            else:
                if min_size>size:
                    min_size = size 
                size = 1

    return min_size
            
for caso in range(1,casos+1):
    N,K = map(int,txt.readline().rsplit())
    menorEspaco = 0
    maiorEspaco = N / 2
    stalls = ""
    if N == K:
        menorEspaco = 0
        maiorEspaco = 0
    # elif N / K < 3:
    #     menorEspaco = 0
    #     maiorEspaco = 1
    # elif N / K == 3 and N % K == 0:
    #     menorEspaco = 1
    #     maiorEspaco = 1
    else:
        
        pessoas = 1
        if N%2 != 0:
            stalls = '.' * (N/2) + '0' + '.' * (N/2)
        else:
            stalls = '.' * ((N/2)-1) + '0' + '.' * (N/2)
        # print stalls
        while pessoas < (K -1):
            posicao, tamanho = longestrun(stalls)
            # print stalls
            # print posicao, tamanho
            stallsInicio = stalls[:posicao]
            stallsTemp = stalls[posicao:posicao + tamanho]
            stallsFim = stalls[posicao+tamanho:]
            # print stallsInicio +"-"+ stallsTemp+"-"+ stallsFim
            stallsTemp = incluirPessoa(stallsTemp)
            stalls = stallsInicio + stallsTemp + stallsFim
            # print stalls
            pessoas += 1
        #print stalls
        if K != 1:
            posicao, tamanho = longestrun(stalls)
        else:
            tamanho = N
        if tamanho % 2 == 0:
            menorEspaco = (tamanho / 2) - 1
            maiorEspaco = (tamanho / 2)
        else:
            menorEspaco = tamanho / 2
            maiorEspaco = menorEspaco
    print("Case #%d: %s %s" %(caso, maiorEspaco, menorEspaco))