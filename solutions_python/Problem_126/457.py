#!/usr/bin/python

import sys

counteds=[]

def CConsAtLeast(name,n):
	count=0
	for c in name:
		if c in 'aeiou':
			count=0
		else:
			count=count+1
		if count>=n:
			return True
	return False			

def recursiveSplit(name,n,start):
	global counteds
	l=len(name)
	total=0

	#base case
	if l<=n:
		if CConsAtLeast(name,n):
			pair=start,name
			if pair not in counteds:
				counteds.append(pair)
				return 1
			return 0
		else:
			return 0
	#splits
	else:
		if CConsAtLeast(name,n):
			pair=start,name
			if pair not in counteds:
				total=1
				total+=recursiveSplit(name[1:],n,start+1)
				total+=recursiveSplit(name[:-1],n,start)
				counteds.append(pair)	
			else:
				total=0

		return total

def processCase(name,n):
	# *** BEGIN CODE PROCESSING CASE ***
	global counteds

	counteds=[]

	nValue=recursiveSplit(name,n,0)

	# *** END CODE PROCESSING CASE ***
	return str(nValue) 

def readCase(case):

	# *** BEGIN CODE READING CASE ***
	caseInput=sys.stdin.readline()

	n=int(caseInput.split()[1])
	name=caseInput.split()[0]

	# *** END CODE READING CASE ***

	solution=processCase(name,n)
	print "Case #"+str(case)+": "+solution

cases=int(sys.stdin.readline())

for case in range(cases):
	readCase(case+1)

