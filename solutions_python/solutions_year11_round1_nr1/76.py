#!/usr/bin/python
# -*- coding: utf-8 -*-

def GGT(a,  b):
    if b == 0:
        return a
    else:
        return GGT(b, a%b)

f = open("in","r");

def readInts():
	return map(int, f.readline().split())

caseCnt = int(f.readline())

for caseNr in range(1, caseCnt + 1):
	#go for it
	print "Case #" + str(caseNr) + ":",
	
	# Read
	N, PD, PG = readInts();
	
	possible = True
	
	# test on PG
	if (PG == 0 and PD != 0) or (PG == 100 and PD != 100):
		possible = False
	else:
		a = PD
		b = 100	
		ggt = GGT(a,b)
		a /= ggt
		b /= ggt
	
		possible =  (b <= N)
		
	
	# Output
	if possible:
		print "Possible"
	else:
		print "Broken"
