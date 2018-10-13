#!/usr/bin/env python3
import sys
argc = len(sys.argv)
filename = sys.argv[1]
if argc > 2:
	casenumbers = list(map(int, sys.argv[2:]))
file = open(filename)
T = int(file.readline().rstrip())
for case in range(1,T+1):
	A, B, K = map(int, file.readline().rstrip().split())
	if argc > 2 and not(case in casenumbers):
		continue
	possiblewins = 0
	for oldnumber in range(A):
		for newnumber in range(B):
			winningnumber = oldnumber & newnumber
			if winningnumber < K:
				possiblewins += 1 
	print ("Case #", case, ": ", sep="", end="")
	print(possiblewins)
