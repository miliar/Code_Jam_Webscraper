import re


linhas = file("entrada.txt").readlines()
L, D, N = linhas.pop(0).rstrip().split(' ')
alfabeto = []

for i in range(int(D)):
	alfabeto.append(linhas.pop(0).rstrip())

for i in range(int(N)):
	padrao = linhas.pop(0).rstrip()
	padrao = padrao.replace('(', '[')
	padrao = padrao.replace(')', ']')
	pattern = re.compile(padrao)
	
	ocorrencias = 0
	for palavra in alfabeto:
		if pattern.match(palavra):
			ocorrencias += 1
	print "Case #%d: %d" % (i+1, ocorrencias)
	
