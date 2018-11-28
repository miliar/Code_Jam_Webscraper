#!/usr/bin/python3
from sys import argv

def trocaPrimeiroMenor(valor):
    numeroAnterior = int(valor[0])
    posicao = 0
    if(len(valor) == 1):
        return valor
    for numero in valor:
        numero = int(numero)
        if(numero < numeroAnterior):
            parteInicial = str(valor[:posicao-1])

            parteMeio = str(numeroAnterior -1)
            parteFinal = "9" * (len(valor)-posicao)
            #print(len(parteInicial))
            if(len(parteInicial)== 0 and parteMeio == "0"):
                parteMeio = ""
            #print ("%s %s %s" %(parteInicial, parteMeio, parteFinal))
            return parteInicial + parteMeio + parteFinal
        numeroAnterior = numero
        posicao += 1
    return valor
script, filename = argv

txt = open(filename)

casos = int(txt.readline())

for caso in range(1,casos+1):
    N = txt.readline().rsplit()[0]
    tidy = trocaPrimeiroMenor(N)
    novoTidy = trocaPrimeiroMenor(tidy)
    while novoTidy != tidy:
        tidy = novoTidy
        novoTidy = trocaPrimeiroMenor(tidy)

        pass



    print("Case #%d: %s" %(caso, novoTidy))