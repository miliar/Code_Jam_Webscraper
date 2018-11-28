#!/usr/bin/env python


inputText = open('input.txt', 'r').read()
outFile = open('output.txt', 'w')

def splitLines():
	return [token.strip() for token in inputText.split('\n')]

def getAnswer(arr):
	s = ""
	for i in xrange(len(arr)):
		s+= str(arr[i])
		
	return s
	
	
def getArray(A):
	

	arr = []
	for i in xrange(len(A)):
		arr.append(int(A[i]))
	
	return arr	
	
def swapWithSmaller(arr, start):
	
	for i in xrange(start+1, len(arr)):
		smallest = float("infinity")
		index = -1
		for j in xrange(i, len(arr)):
			if(arr[j] < arr[i]):
				if(arr[j] < smallest):
					smallest = arr[j]
					index = j
		if(index > -1):
			swap = arr[i]
			arr[i] = arr[index]
			arr[index] = swap
			
	return arr				



	
def isSpecialCase(arr):
	if(arr[len(arr)-1] > 0):
		return False
	
	for i in xrange(1,len(arr)):
		if (arr[i] > arr[i-1]):
			return False
	return True

def fix(arr):
	for i in xrange(1, len(arr)):
		if(arr[i]>0):
			arr[0] = arr[i]
			arr[i] = 0
			return arr	
	
			
def getNextinSeq(nr):
	a = getArray(nr)
	
	if (isSpecialCase(a)):
		
		a.sort()
		if (a[0] == 0):
			a = fix(a)
		a.insert(1,0)
		swapWithSmaller(a,1)
		return a
	#for each digit from right to left
	for i in xrange(len(a)-1,-1,-1):
		
		smallest = float("infinity")
		index = -1
		for j in xrange(i+1,len(a)):
			if((a[j] > a[i])):
				if(a[j] < smallest):
					smallest = a[j]
					index = j
		if(index > -1):
			swap = a[i]
			a[i] = a[index]
			a[index] = swap
			swapWithSmaller(a,i)
			return a
		
	
	#If we reach here, we need to introduce a zero or a 1:
	
	a.sort()
	a.insert(1,0)
	swapWithSmaller(a,1)
	return a

	
	
	
if __name__ == "__main__":
	
	splittedInput = splitLines()
	nrCases = int(splittedInput[0])

	for i in xrange(1,nrCases+1):
		answer = getNextinSeq(splittedInput[i])
		outString = "Case #"+str(i)+":"+" "+getAnswer(answer)+"\n"
		outFile.write(outString)	
		
	outFile.close()	