#!/usr/bin/env python
# -*-coding: latin1-*-

#speaking.py
#Autor: Anderson Berg
#14/04/2012

letras = {'y':'a', 'n':'b', 'f':'c', 'i':'d', 'c':'e', 'w':'f', 'l':'g', 'b':'h', 'k':'i', 'u':'j', 'o':'k', 'm':'l', 'x':'m', 's':'n', 'e':'o', 'v':'p', 'z':'q', 'p':'r', 'd':'s', 'r':'t', 'j':'u', 'g':'v', 't':'w', 'h':'x', 'a':'y', 'q':'z'}




def traduz_palavra(palavra):
    palavra_traduzida = ''
    for letra in palavra:
        palavra_traduzida = palavra_traduzida + letras[letra]

    return palavra_traduzida


def resolve_caso(arquivo):
    traducao_lista = []
    frase = arquivo.readline()
    palavras = frase.split()
    for palavra in palavras:
        palavra_traduzida = traduz_palavra(palavra)
        traducao_lista.append(palavra_traduzida)

    traducao = ''
    for palavra in traducao_lista:
        traducao = traducao + palavra + ' '

    return traducao



def main():
    arquivo = open('A-small-attempt0.in', 'r')
    casos = arquivo.readline()
    n_casos = int(casos)

    saida = open('output.out', 'w')
    text = []
    for i in range(n_casos):
        texto = resolve_caso(arquivo)
        text.append('Case #%d: %s\n' % (i+1, texto))

    saida.writelines(text)
    saida.close()


if __name__ == '__main__':
    main()
