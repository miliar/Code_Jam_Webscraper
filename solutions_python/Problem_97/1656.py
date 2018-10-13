#!/usr/bin/env python
#-*- coding:utf-8 -*-

def pares(a, b):
	res = 0
	for n in range(a, b):
		listan = []
		for size in range(0, len(str(n))-1):
			ind = -1-size
			cad_n = str(n)
			m = cad_n[ind:len(cad_n)] + cad_n[:ind]
			if n < int(m) and int(m) <= b and len(str(int(m))) == len(cad_n) and \
			not (int(m) in listan):
				res += 1
				listan.append(m)
	return res
	

fichero_in = open("/home/blacknack/Escritorio/C-small-attempt0.in", "r")
fichero_out = open ("/home/blacknack/Escritorio/cout.txt", "w")

nlineas = int(fichero_in.readline())

for i in range(nlineas):
	linea = fichero_in.readline()
	l = linea.split()
	a = l[0]
	b = l[1]
	res = pares(int(a), int(b))
	fichero_out.write("Case #" + str(i+1) + ": ")
	fichero_out.write(str(res) + "\n")
