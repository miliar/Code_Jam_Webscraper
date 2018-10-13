#!/usr/bin/python

import sys

file = open(sys.argv[1])
text = file.read()
file.close()
lines = text.split("\n")

T = int(lines[0])

case = []

for i in range(0,T*2,2):
	n = len(case)
	case.append(0)

	g = lines[i+1].split(' ')
	g = [int(x) for x in g]
	R = g[0]
	k = g[1]
	N = g[2]
	g = lines[i+2].split(' ')
	g = [int(x) for x in g]
	for j in range(R):
		current = 0
		Ni = 0
		tmp = []
		for x in range(len(g)):
			if(Ni > N): break
			if(current+g[x] > k): break
			tmp.append(g[x])
			Ni += 1
			current+=g[x]
		case[n] += current
		g = g[Ni:] + g[:Ni]

for i in range(len(case)):
	print "Case #"+str(i+1)+": "+str(case[i])
