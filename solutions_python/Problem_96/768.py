#!/usr/bin/python 
from sys import argv
import re
from math import pow,floor,log10

def getNumber(args):
	num = args[0]
	special = args[1]
	atleast = args[2] 
	count = 0
	for v in args[3:]:
		first = int(v/3)
		second = int((v-first)/2)
		third = v-first-second
		#print "%d\t%d\t%d\t%d" %(v,first,second,third)
		maxi = max([first,second,third])
		if maxi >= atleast:
			count +=1 
			continue
		if special == 0:
			continue
		mini = min([first,second,third]) 
		if maxi-mini <2 and maxi +1 >= atleast and mini -1 >=0 :
			special -=1
			count +=1
	return count
			
		


with open(argv[1],'r') as f:
	numCases = int(f.readline())
	casenum = 1
	while(casenum <= numCases):
		line = f.readline().strip()
		params = re.split("\s+",line)
		print 'Case #%d: %d' %(casenum,getNumber(map(int,params)))
		casenum +=1
