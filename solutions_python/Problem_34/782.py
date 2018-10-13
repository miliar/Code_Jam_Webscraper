#! /usr/bin/python
import os
import sys
import glob
from math import sqrt

if len(sys.argv) != 2:
	print 'USAGE: q1.py input.in'
	sys.exit()

fIn = open(sys.argv[1], 'r')
param = fIn.readline().split()
L = int(param[0])
D = int(param[1])
N = int(param[2])
#print str(L)+str(D)+str(N)
dict = []
for i in range(D):
	dict.append(fIn.readline()[:-1])

#print dict
tokens = ['' for i in range(L)]
#print len(tokens)

for i in range(N):
	line = fIn.readline()[:-1]
	pos = 0
	for j in range(L):
		m = line[pos]
		if m != '(' and m != ')':
			tokens[j] = m
			pos = pos + 1
		if m == '(':
			while(1):
				pos = pos + 1
				m = line[pos]
				if m == ')': 
					pos = pos + 1
					break
				tokens[j] += m
		j = j + 1
#	print tokens
	count = 0
	for j in range(D):
		tag = 1
		word = dict[j]
#		print word
		for pos in range(L):
			if tokens[pos].count(word[pos]) == 0:
				tag = 0
#				print 'NOT'
				break
		if tag == 1:
			count = count + 1
			
		
	
	print 'Case #'+str(i+1)+': '+str(count)
	tokens = ['' for i in range(L)]
#	print '\n'
