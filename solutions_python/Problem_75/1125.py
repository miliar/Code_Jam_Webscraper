#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Alberto Barrionuevo Castillo on 2011-05-07.
Copyright (c) 2011 Darko. All rights reserved.
"""

def oposition(elements, op, opposittes):
	for e in elements:
		if e in opposittes:
			if opposittes[e] == op:
				return True
	return False

def p(lista):
	if len(lista) == 0:
		return '[]'
	elif len(lista) == 1:
		return '[' + lista[0] + ']'
	else:
		res = '[' + lista[0]
		for e in lista[1:]:
			res += ', ' + e
	return res + ']'
	

f = open('B-small-attempt0.in')
aux = f.readline()
for i in range(0, int(aux)):
	magic = f.readline().strip()
	combinations = {}
	opposed = {}
	element = []
	magic = magic.partition(' ')
	for j in range(0, int(magic[0])):
		magic = str(magic[2])
		magic = magic.partition(' ')
		c = magic[0]
		combinations[c[0]+c[1]] = c[2]
		combinations[c[1]+c[0]] = c[2]
	magic = str(magic[2])
	magic = magic.partition(' ')
	for k in range(0, int(magic[0])):
		magic = str(magic[2])
		magic = magic.partition(' ')
		o = magic[0]
		opposed[o[0]] = o[1]
		opposed[o[1]] = o[0]
	magic = str(magic[2])
	magic = magic.partition(' ')
	cad = magic[2]
	for m in range(0, int(magic[0])):
		e = cad[m]
		if len(element) == 0:
			element = [e]
		else:
			aux2 = e+element[-1] in combinations
			if aux2:
				aux3 = combinations[e+element[-1]]
			else:
				aux2 = element[-1]+e in combinations
				if aux2:
					aux3 = combinations[element[-1]+e]
			if aux2:
				if oposition(element, aux3, opposed):
					element = []
				else:
					element[-1] = aux3
			else:
				if oposition(element, e, opposed):
					element = []
				else:
					element.append(e)
	print "Case #%d: " % (i+1), p(element)