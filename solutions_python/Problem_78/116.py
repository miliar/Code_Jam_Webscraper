#!/usr/bin/env python
import sys
infile = sys.argv[1]
#outfile = sys.argv[2]

indata = open(infile, 'r').readlines()
#print indata

numcases = int(indata[0].strip())
cases = [x.strip().split(' ') for x in indata[1:]]

for j in range(0, numcases):
	case = cases[j]
	N = int(case[0])
	PD = int(case[1])
	PG = int(case[2])
	#Solve case
	F = 1
	X = PD
	if X == (X/5)*5:
		F = F*5
		X = X/5
	if X == (X/5)*5:
		F = F*5
		X = X/5
	if X == (X/2)*2:
		F = F*2
		X = X/2
	if X == (X/2)*2:
		F = F*2
		X = X/2

	if PG == 100:
		sol = PD == 100
	elif PG == 0:
		sol = PD == 0
	else:
		sol = 100/F <= N

	if sol:
		print "Case #" + str(j+1) + ": " + "Possible"
	else:
		print "Case #" + str(j+1) + ": " + "Broken"
