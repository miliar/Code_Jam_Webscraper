import math

def isFairSquare(n):
	if isPalindrome(n):
		if math.sqrt(n).is_integer():
			if isPalindrome(int(math.sqrt(n))):
				return True
	return False

def isPalindrome(n):
	forward = str(n)
	backward = forward[::-1]
	if forward == backward:
		return True
	else:
		return False




f = open('C-small-attempt1.in', 'r')
T = int(f.readline())
for i in range(T):
	counter = 0
	line = f.readline().split()
	min = int(line[0])
	max = int(line[1])
	for j in range(max-min+1):
		if isFairSquare(j + min):
			counter += 1
	print "Case #" + str(i + 1) +  ": " + str(counter)
