#!/usr/bin/python

import sys

def movesRequired(stack, minTime):
	required = 0

	for i in range(len(stack)):
		if stack[i] <= minTime:
			 continue
		required += (stack[i] + minTime - 1)//minTime - 1
	
	return required
		
def minStack(stack):
	minimum = 1000

	for i in range(1, 1000):
		minimum = min(minimum, i + movesRequired(stack, i))
	
	return minimum

if __name__ == "__main__":
	cases = int(sys.stdin.readline())

	for i in range(cases):
		total = int(sys.stdin.readline())
		stacks = map(int, sys.stdin.readline().split())
		stacks.sort()
		stacks.reverse()

		print "Case #{0}: {1}".format(str(i+1), minStack(stacks))
