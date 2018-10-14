#!/usr/bin/python

from scipy import *
import sys

#Q=0, W=1, E=2, R, A, S, D, F : base
now = 0
code = {}
for c in "QWERASDF":
	code[c] = now
	now += 1

now = 8
for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
	if c not in code:
		code[c] = now
		now += 1
#print code,len(code)

decode = {}
for key,value in code.items():
	decode[value] = key
#print decode


T = int(raw_input())

for test_case in range(T):
	rule = zeros((26,26),dtype='int')
	delete_rule = zeros((26,26),dtype='int')
	
	line = raw_input()
	C = int(line[0:line.find(" ")])
	line = line[line.find(" ")+1:]
	for c in range(C):
		r = line[:line.find(" ")]
		line = line[line.find(" ")+1:]
		rule[code[r[0]],code[r[1]]] = code[r[2]]
		rule[code[r[1]],code[r[0]]] = code[r[2]]

	D = int(line[0:line.find(" ")])
	line = line[line.find(" ")+1:]
	for c in range(D):
		r = line[:line.find(" ")]
		line = line[line.find(" ")+1:]
		delete_rule[code[r[0]],code[r[1]]] = -1
		delete_rule[code[r[1]],code[r[0]]] = -1
		
	N = int(line[0:line.find(" ")])
	line = line[line.find(" ")+1:]
	target = [code[c] for c in line]
	now = []

	for c in target:
		if len(now) == 0:
			now.append(c)
		else:
			last = now[len(now)-1]
			r = rule[last,c]
			if r != 0:
				del now[len(now)-1]
				now.append(r)
			else:
				#r == -1
				for check in now:
					if delete_rule[check,c] == -1:
						now = []
				if len(now) != 0:
					now.append(c)
	result = []
	write = sys.stdout.write

	write("Case #%d: [" % (test_case+1))
	for i in range(len(now)):
		write(decode[now[i]])
		if i != len(now)-1:
			write(", ")
	print "]"
