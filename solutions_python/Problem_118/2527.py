# finding square palindromes

# probably the most efficient way of doing this is finding each 
# palindrome within the bounds, squaring it, and seeing if that
# square is a palindrome as well. If it is, increment the counter

import sys, math

def isPalindrome(number):
	strNum = str(number)
	strNum = list(strNum)

	newStr = ""
	for i in xrange(len(strNum)):
		newStr += strNum.pop()

	newInt = int(newStr)

	if(number == newInt):
		return True

	return False

numCases = int(raw_input())

for x in xrange(numCases):
	palCount = 0 # number of fair and square numbers we've found

	inp = sys.stdin.readline().split() # get the lower and upper bounds
	lowBound = int(inp[0])
	upBound = int(inp[1])

	for j in xrange(lowBound, upBound + 1):
		if(isPalindrome(j)):
			# find out if it's the square of a palindrome too
			sqrtJ = math.sqrt(j)
			# print sqrtJ

			if(sqrtJ % 1 == 0):
				if(isPalindrome(int(sqrtJ))):
					palCount += 1
					# print sqrtJ
				

	print "Case #" + str(x + 1) + ": " + str(palCount)
