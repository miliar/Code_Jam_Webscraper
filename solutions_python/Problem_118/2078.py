#!/usr/bin/python
import math

def main():
	inputFile = open('test.in','r')
	testCases = int(inputFile.readline())
	for i in xrange(testCases):
		limits = inputFile.readline().split(' ')
		lowerLimit = int(limits[0])
		upperLimit = int(limits[1])
	
		count = 0
		for j in range(lowerLimit,upperLimit+1):		
			square = list(str(j))
			reverseSquare = []
			reverseSquare.extend(square)
			reverseSquare.reverse()
			if isSquare(j) and square == reverseSquare:
				print 'j= '+str(j)+' is square'
				number = int(math.sqrt(j))
				number = list(str(number))
				reverseNumber = []
				reverseNumber.extend(number)
				reverseNumber.reverse()
				if number == reverseNumber:
					count = count + 1
	
		outputFile = open('test.out','a+')
		outputFile.write('Case #'+str(i+1)+': '+str(count)+'\n')
		outputFile.close()
	
def isSquare(integer):
	root = math.sqrt(integer)
	if int(root + 0.5) ** 2 == integer: 
		return True
	else:
		return False
        
main()
