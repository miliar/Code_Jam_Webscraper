def lastTidy(N):
	if N < 10:
		return N

	foundNumTidy = False

	while N >= 10 and not foundNumTidy:
		countSteps = 0
		lastDigit = N % 10
		tempNum = N / 10
		countSteps += 1
		numTidy = True

		while numTidy:
			nextDigit = tempNum % 10
			if nextDigit > lastDigit:
				numTidy = False
				N = tempNum * (10**countSteps) - 1
			elif tempNum < 10:
				foundNumTidy = True
				numTidy = False
			countSteps += 1
			tempNum /= 10
			lastDigit = nextDigit
			if N < 10:
				foundNumTidy = True
				numTidy = False

	return N


def main():
	# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
	# This is all you need for most Google Code Jam problems.
	t = int(raw_input())  # test cases
	for i in xrange(1, t+1):
		N = int(raw_input())
	  	print "Case #{}: {}".format(i,lastTidy(N))
	  	#n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
	  	#print "Case #{}: {} {}".format(i, n + m, n * m)
	  	# check out .format's specification for more formatting options


if __name__=='__main__':
	main()
