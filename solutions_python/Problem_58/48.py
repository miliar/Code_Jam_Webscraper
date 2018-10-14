import sys
from fractions import gcd

def parseInput():
	cases = []

	data = [x.strip() for x in sys.stdin.readlines()]

	T = int(data.pop(0))
	for elem in data:
		cases.append(tuple([int(x) for x in elem.split(' ')]))

	return cases

def isWinning(A, B):
	d = gcd(A, B)

	A /= d
	B /= d

	if A == 1 and B == 1:
		return False

	if A == 1 or B == 1:
		return True

	a = max(A, B)
	b = min(A, B)

	if b < a / 2:
		return True

	return not isWinning(b, a - b)

def solve(A1, A2, B1, B2):
	counter = 0
	for A in xrange(A1, A2 + 1):
		for B in xrange(B1, B2 + 1):
			if isWinning(A, B):
				counter += 1

	return str(counter)

cases = parseInput()
for num, case in enumerate(cases):
	result = solve(*case)
	print "Case #" + str(num + 1) + ": " + result
