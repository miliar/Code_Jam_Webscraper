#!/usr/bin/env python
import math
import sys
import os
from os import system

def calculate(comb,oppo,invoke):
	ret = []
	ret.append(invoke[0])
	for i in range(len(invoke)-1):
		ink = invoke[i+1]
		if len(ret) > 0:
			key1 = ret[-1]+ink
			key2 = ink+ret[-1]
			ifadd = True
			if key1 in comb:
				ret.pop()
				ret.append(comb[key1])
				ifadd = False
			elif key2 in comb:
				ret.pop()
				ret.append(comb[key2])
				ifadd = False
			else :
				for r in ret:
					key1 = r+ink
					key2 = ink+r
					if key1 in oppo:
						ret = []
						ifadd = False
						break
					elif key2 in oppo:
						ret = []
						ifadd = False
						break
			if ifadd:
				ret.append(ink)
		else :
			ret.append(ink)
	
	#print ret
	return ret




fp = open(sys.argv[1],'r')
fout = open(sys.argv[2],'w')
str = fp.readline()
T = int(str)
for i in range(T):
	l = fp.readline().split()
	index = 0
	C = int(l[0])
	index += 1
	comb = {}
	for j in range(C):
		key = l[j+1][0:2]
		comb[key] = l[j+1][2]
		index += 1
	#print comb
	
	D = int(l[index])
	index += 1
	oppo = []
	for j in range(D):
		oppo.append(l[j+index])
	index += D
	#print oppo

	N = int(l[index])
	index += 1
	invoke = []
	for j in range(N):
		invoke.append(l[index][j])
	#print invoke


	ret = calculate(comb,oppo,invoke)

	fout.write('Case #%d: ['%((i+1)))
	for i in range(len(ret)):
		fout.write('%s'%ret[i])
		if i is not (len(ret)-1):
			fout.write(', ')
	fout.write(']\n')
