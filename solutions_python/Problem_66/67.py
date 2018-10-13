#!/usr/bin/env python
import math
import sys
import os
from os import system


fp = open(sys.argv[1],'r')
fout = open(sys.argv[2],'w')
str = fp.readline()
T = int(str)
for i in range(T):
	p = int(fp.readline())
	M = []
	for tk in fp.readline().split():
		M.append(int(tk))
	for j in range(p):
		l = fp.readline()
	num = 2**p
	game = []
	for j in range(p):
		game.append([0]*(2**(p-j-1)))
	print game
	print M
	for j in range(p):
		for k in range(num):
			if M[k] == j:
				for m in range(p-j):
					game[p-m-1][k/(2**(p-m))] = 1
	summ = 0
	for gg in game:
		summ = summ + sum(gg)
	fout.write('Case #%d: %d\n'%(i+1,summ))
