#!/usr/bin/python

import sys

globalSet=set()

def recicledList(nums):
	l=[]

	tam=len(nums)
	for i in xrange(tam):
		if i>0:
			firsthalf=nums[:i]
			secondhalf=nums[i:tam]
			l.append(secondhalf+firsthalf)
	
	return l;

def findRecInRange(min,num):

	global globalSet
	nums=str(num)
	candidates=recicledList(nums)	
	valid=0

	for candidate in candidates:
		if int(candidate)>=min:
			if int(candidate)<num:
				globalSet.add(str(candidate)+str(num))

	return

def processCase(case):
	# *** BEGIN CODE PROCESSING CASE ***

	global globalSet
	limits=case.split()

	min=int(limits[0])
	max=int(limits[1])

	globalSet=set()

	for num in xrange(min,max+1):
		findRecInRange(min,num)

	# print globalSet
	# *** END CODE PROCESSING CASE ***
	return len(globalSet)

def readCase(case):

	# *** BEGIN CODE READING CASE ***
	caseInput=sys.stdin.readline()
		
	# *** END CODE READING CASE ***

	solution=processCase(caseInput)
	print "Case #"+str(case)+": "+str(solution)

cases=int(sys.stdin.readline())

for case in range(cases):
	readCase(case+1)

