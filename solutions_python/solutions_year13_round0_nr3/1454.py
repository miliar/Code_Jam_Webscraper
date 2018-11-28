
import math;

def line2intlist(line):
    list = line.split()
    numbers = [ int(x) for x in list ]
    return numbers

def isPalindrome(i):
	s = str(i)
	return s == s[::-1]
	
def countSquares(start, end):
	count = 0
	startInSqrtSpace = int(math.ceil(math.sqrt(start)))
	endInSqrtSpace = int(math.floor(math.sqrt(end)))
	for i in xrange(startInSqrtSpace, endInSqrtSpace + 1):
		if isPalindrome(i):
			if isPalindrome(i * i):
				#print i, i* i
				count += 1
	
	return count
	
testcases = input()

for caseNum in xrange(0, testcases):
	interval = line2intlist(raw_input())
	count = countSquares(interval[0], interval[1])
	print("Case #%i: %s" % (caseNum + 1, count))
