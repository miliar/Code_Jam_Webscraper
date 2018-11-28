#Fair and Square

import sys, fileinput, math

def isPalindrome(n):
	#check from beginning and end and converge
	nString = str(n)
	head = 0
	tail = len(nString) - 1
	while( (tail - head) > 1 ):
		#check if equal
		if (nString[head] == nString[tail]):
			head += 1
			tail -= 1
		else:
			return False
	# reached the middle point 
	if (nString[head] == nString[tail]):
		return True
	else:
		return False
	

def findFairAndSquare(a,b):
	y = 0 #number of fair and square numbers
	# find square root >= a, and square root <=b
	a_root = int(math.ceil(math.sqrt(a)))
	b_root = int(math.floor(math.sqrt(b)))
	# input must also be palindrome
	for inputP in range(a_root,b_root+1):
		if isPalindrome(inputP):
			if isPalindrome(int(math.pow(inputP,2))):
				y += 1
	return y


def solve():
	#output file
	out = open('output','w') 
	

	#input file
	filein = fileinput.input()
	#set up test cases
	caseInt = 1
	totalTests = 0
	
	#process
	for line in filein:
		if filein.isfirstline():
			totalTests = int(line)
		else:
			#break into A and B
			ABinput = line.split(' ',2)
			outValue = findFairAndSquare(int(ABinput[0]),int(ABinput[1]))
			#write out
			out.write('Case #' + str(caseInt) + ': ' + str(outValue) + '\n')
			caseInt += 1
			if caseInt > totalTests:
				break;
	out.close
	
solve()

