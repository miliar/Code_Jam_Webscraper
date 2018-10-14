#!/usr/bin/env python

import math, sys

def Check(numList):
	length = len(numList)
	if length != 1:
		for i in range(0, length/2):
			if numList[i] != numList[length-1-i]:
				return False
	return True
		
def NumToList(num):
    return list("%d" % num)

def ListToNum(numList):
	if len(numList) == 1:
		return int(numList[0])
	else:
		s = ''.join(map(str, numList))
		return int(s)

def CountNines(numList):
	count = 0
	for i in numList:
		if i == 9:
			count += 1
	return count
	
def CreateFirstWithLength(length):
	numList = [1]
	for i in range(1,length-1):
		numList.append(0)
	numList.append(1)
	return numList
	
def CreateFirstNextTo(numList):
	length = len(numList)
	if length == 1:
		return numList
	if numList[0] < numList[length-1]:
		val = numList[0] + 1
		numList = CreateFirstWithLength(length)
		numList[0] = numList[length-1] = val
		return numList
	else:
		numList[length-1] = numList[0] # x...x
		
	if length % 2 == 0:
		if length != 2:
			if numList[1] > numList[2]:
				for i in range(2, length-1):
					numList[i] = numList[1]
			else:
				val = numList[1] + 1
				for i in range(1, length-1):
					numList[i] = val
	else:
		if length != 3:
			mid = length/2
			flist = numList[1:mid]
			llist = numList[mid+1:length-1]
			val = ListToNum(flist)
			if val >= ListToNum(llist):
				numList[mid+1:length-1] = flist[::-1]
			else:
				val = val + 1
				val = NumToList(val)
				nval = []
				lval = len(val)
				lflist = len(flist)
				diff = lflist - lval
				while(len(nval) < diff):
					nval.append(0)
				nval += val
				numList[1:mid] = nval
				numList[mid+1:length-1]	= nval[::-1]
	for i in range(0, len(numList)): # str to int
		numList[i] = int(numList[i])	
	return numList

def NextPalindrome(numList):
	length = len(numList)
	mid = int(length/2)
	# number of digits is even
	if mid*2 == length:
		val0 = numList[0]
		val1 = numList[1]
		if(val1 == 9):
			if(val0 == 9):
				return CreateFirstWithLength(length+1)
			else:
				numList = CreateFirstWithLength(length)
				numList[0] = numList[length-1] = numList[0] + val0
		else:	
			val1 = val1 + 1
			if length == 2:
				for i in range(0,length):
					numList[i] = val1
			else:
				for i in range(1,length-1):
					numList[i] = val1
		return numList
	# number of digits is odd
	else:
		count = CountNines(numList)
		# 99..9999
		if count == length:
			numList = CreateFirstWithLength(length+1)
			return numList
		# other...
		else:				
			if numList[mid] == 9:
				d = 0
				while numList[mid+d] == 9:
					numList[mid] = numList[mid-d] = numList[mid+d] = 0
					d += 1
				numList[mid-d] = numList[mid+d] = numList[mid-d] + 1
			else:
				numList[mid] = numList[mid] + 1			
		# returning	
		return numList		
		
########

T = sys.stdin.readline()
T = T.strip()
T = int(T)

for t in xrange(T):
	R = sys.stdin.readline()
	R = R.strip()
	R = R.split(' ')
	start = int(math.sqrt(float(R[0])))
	end = int(math.sqrt(float(R[1])))
	if start**2 < float(R[0]):
		start += 1
	start = NumToList(start)
	for i in range(0, len(start)):
		start[i] = int(start[i])
	if not Check(start):
		start = CreateFirstNextTo(start)
	count = 0
	while(True):
		if not ListToNum(start) <= end:
			break
		else:
			if Check(NumToList(ListToNum(start)**2)): 
				count += 1
			start = NextPalindrome(start)
	sys.stdout.write('Case #' + str(t+1) + ': ' + str(count))
	if(t != T-1): 
		print