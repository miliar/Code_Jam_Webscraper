import math

input_file = open('csmall.txt')

countlines = 0

def isPalindrome(num):
	string = str(num)
	for i in xrange(len(string)/2+1):
		if string[i] != string[len(string) - i - 1]:
			return False
	return True

def isSquare(num):
	squareroot = num**0.5
	if squareroot - int(squareroot) == 0.0:
		return True
	return False

def isSquareAndFair(num):
	if not(isPalindrome(num)):
		return False
	if not(isSquare(num)):
		return False
	if not(isPalindrome(int(num**0.5))):
		return False
	return True

for line in input_file:
	if countlines == 0:
		# numOfCases = int(line)+1
		countlines+=1
		continue
	start,end = line.split(" ")
	start = int(start)
	end = int(end)
	squaresAndFairs = 0
	for i in xrange(start,end+1):
		if isSquareAndFair(i):
			squaresAndFairs+=1
	print 'Case #' + str(countlines) + ': ' + str(squaresAndFairs)
	countlines +=1