#!/usr/bin/python
import sys
import re

_dprint = False

def _output(case, answer):
	print "Case #{0}: {1}".format(case, answer)

# get number of cases
infile = open(sys.argv[1],'r')
cases = int(infile.readline())

for case in range(1,1+cases):
	if _dprint: print "******** Starting Case:",case
	wires = []
	N = map(int,re.findall(r'\d+',infile.readline()))[0]
	for i in range(N):
		(e1, e2) = map(int,re.findall(r'\d+',infile.readline()))
		wires.append([e1, e2])
	wires.sort(lambda x,y: cmp(x[0],y[0]))
	crossings = 0
	for i in range(N):
		for j in range(i,N):
			if wires[i][1] > wires[j][1]: crossings += 1
	_output(case,crossings)
infile.close()
