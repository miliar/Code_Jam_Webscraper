# coding: utf-8

import math
import sys

def lampada_acesa(N,K):
	#nega o valor e extrai o primeiro bit 1, que é a mesma coisa que extrair o
	#primeiro bit 0 do número original
	x = ~K
	y = x & -x
	#compara se a lâmpada pode estar acesa:
	# se 2**N-1 for menor ou igual a y, então tem enegia da fonte até a lâmpada
	if 1 << N  <= y:
		return "ON"
	else:
		return "OFF"

with open(sys.argv[1]) as arq:
	with open("saida.out", "w") as saida:
		T = int(arq.readline().strip('\n'))
		for caso in range(1, T+1):
			linha = arq.readline().strip('\n').split()
			N = int(linha[0])
			K = int(linha[1])
			saida.write("Case #" + str(caso) + ": " + lampada_acesa(N,K) + '\n')





