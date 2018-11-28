#!/usr/bin/python 
from sys import argv
import re
from math import pow,floor,log10

def getNumber(A,B):
	count = 0
	for x in range(A,B+1):
		found = set()
		length = int(floor(log10(x))+1) 
		for i in range(1,length):
			base = pow(10,i)
			mul = pow(10,length -i)
			num = int(((x%base)*mul) + (x/base))
			if num > x and num <= B and num not in found:
				found.add(num)
				count +=1
	return count
			
			
		
	

with open(argv[1],'r') as f:
	numCases = int(f.readline())
	casenum = 1
	while(casenum <= numCases):
		line = f.readline().strip()
		A,B = re.split("\s+",line)
		print 'Case #%d: %d' %(casenum,getNumber(int(A),int(B)))
		casenum +=1
