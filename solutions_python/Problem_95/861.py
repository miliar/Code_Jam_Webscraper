#!/usr/bin/env python

import urllib, urllib2, cookielib
import re #biblioteca que procura expressao regular
import os #roda o programa em C que trata a entrada gerada

from sys import argv

f = open('ex_entrada.txt','r')
o = open('ex_saida.txt', 'r')

number = int(f.readline())

mapa1 = []
mapa2 = []
for i in range(number):
	a = f.readline()
	b = o.readline()
	for i in range(0, len(a)):
		mapa1.append(a[i])
		mapa2.append(b[i])
f.close()
o.close()

entrada = open('A-small-attempt3.in', 'r')
saida = open('A-small-attempt3.out', 'w')

number = int(entrada.readline())
sentences = ''
for i in range(number):
	sentences += "Case #" + str(i+1) + ': ' 
	for j in entrada.readline():
		if j in mapa1:
			sentences += mapa2[mapa1.index(j)]

saida.write(sentences)

entrada.close()	
saida.close()