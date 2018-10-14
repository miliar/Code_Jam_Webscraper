#! /usr/bin/python
import os
import sys
from math import sqrt

def transform(n, i):
	N = []
	while n > 0:
		mod = n % i
		n /= i
		N.append(mod)
	return N

if len(sys.argv) != 2:
	print 'USAGE: q1.py input.in'
	sys.exit()

fIn = open(sys.argv[1], 'r')
param = fIn.readline().split()
caseNo = int(param[0])
for i in range(caseNo):
	num = fIn.readline().split()[0]
	numList = [0,0,0,0,0,0,0,0,0]
	for j in num:
		curNum = int(j)
		if curNum == 0:
			continue
		numList[curNum-1] += 1
	number = int(num)
	
	while(1):
		numList1 = [0,0,0,0,0,0,0,0,0]
		number += 1
		string = str(number)
		for j in string:
			curNum = int(j)
			if curNum == 0:
				continue
			numList1[curNum-1] += 1
		if numList == numList1:
			break
	print 'Case #'+str(i+1)+': '+str(number)


