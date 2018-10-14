import math

def isTidy(i):
	digits = math.floor(math.log10(i))
	largestDigitSoFar = 9
	for power in range(int(digits)+1):
		currentDigit = i % 10**(power+1) / 10**power

		if currentDigit > largestDigitSoFar:
			return False
		else:
			largestDigitSoFar = currentDigit


	return True


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	
	n = [int(s) for s in raw_input().split(" ")][0]  # read a list of integers, 2 in this case

	returnNum = n
	while True:
		if isTidy(returnNum):
			print "Case #{}: {}".format(i, returnNum)
			break
		else:
			# if its not a tidy number can we cheat ahead?
			
			# print returnNum
			returnNum -= 1
	# check out .format's specification for more formatting options
