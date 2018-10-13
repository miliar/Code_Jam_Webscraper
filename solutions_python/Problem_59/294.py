from __future__ import division
import sys
import os


arquivo = open('a_small.in','r')
saida = open('a_small.out', 'w')


quantos = int(arquivo.readline())

def checa_dict(dicionario, caminho):
    if not caminho:
        return 0
    if caminho[0] in dicionario and len(caminho) > 1:
        return checa_dict(dicionario[caminho[0]], caminho[1:])
    elif caminho[0] in dicionario:
        return 0
    elif len(caminho) != 1:
        dicionario[caminho[0]] = {}
        return 1+checa_dict(dicionario[caminho[0]], caminho[1:])
    elif len(caminho) == 1:
        dicionario[caminho[0]] = {}
        return 1
        

for i in range(1, quantos+1):
    conhecidos, novos = arquivo.readline().split(' ')
    conhecidos = int(conhecidos)
    novos = int(novos)
    mkdir = 0
    diretorios = {}
    
    if conhecidos:
        for x in range(conhecidos):
            caminho = arquivo.readline().rstrip().split('/')[1:]
            teste = checa_dict(diretorios, caminho)           
            
    if novos:
        for x in range(novos):
            caminho = arquivo.readline().rstrip().split('/')[1:]
            mkdir += checa_dict(diretorios, caminho)
            
    print diretorios
    saida.write('Case #%i: %i\n' % (i, mkdir))

arquivo.close()
saida.close()