#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

palavras = []

l, d, n = [ int(x) for x in input().split(' ') ]
for i in range(d):
	palavra = input()
	palavras.append(palavra)
	

for i in range(n):
	pattern = input()
	pattern = pattern.replace("(", "[")
	pattern = pattern.replace(")", "]")
	cont = 0
	for palavra in palavras:
		resultado = re.search(pattern, palavra)
		if resultado:
			cont += 1
	print("Case #%d: %d" % (i+1, cont))
