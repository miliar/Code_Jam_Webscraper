import sys
import math

def solve(R, C, W):
	if(W == C):
		return (R - 1) + W

	elif(W > 1):
		rest = (R - 1) * (C - 1)/W
		last = (C - 1)/W + 1 + (W - 1)
		return rest + last
	
	else:
		return R * C
if __name__ == '__main__':

	if (len(sys.argv) < 2):
		f = open('testa', 'r')

	else:
		f = open(sys.argv[1], 'r')

	testCases = int(f.next())
	
	for caseNum in xrange(1, testCases + 1):

		R, C, W = f.next().split()

		R = int(R)
		C = int(C)
		W = int(W)

		answer = solve(R, C, W)

		print('Case #%s: %s' % (caseNum, answer))
