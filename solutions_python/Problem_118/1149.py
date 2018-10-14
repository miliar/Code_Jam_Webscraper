# -*-coding:utf-8 -*-

# Google code jam, qualification round, problem C, fair and square

import numpy as np
import sys

fn = "C-small-attempt0.in"
infile = open(fn,'r')
outfile = open("fairsquare.out",'w')

def ispalingrome(n):
	nstr = str(n)
	l = len(nstr)
	for i in range(0,l/2):
		if nstr[i]!=nstr[l-i-1]:
			return False
	return True

cn = int(infile.readline().strip())
for i in range(0, cn):
	A, B = map(int, infile.readline().strip().split())
	count = 0
	a = int(np.sqrt(A))
	if a*a < A:
		a = a+1
	b = int(np.sqrt(B))
	for n in range(a, b+1):
		if ispalingrome(n) and ispalingrome(n*n):
			count += 1
	outfile.write("Case #" + str(i+1) + ": " + str(count) + "\n")

infile.close()
outfile.close()