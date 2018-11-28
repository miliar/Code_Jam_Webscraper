#!/usr/bin/python2.6
import re, operator

def patrickSum(lst):
	return reduce(operator.xor, lst)

def solve(count, values):
	# If both piles will have the same value, there must be an even number
	# of 1s for all digits. So the xor of all values should be 0.
	if patrickSum(values) > 0:
		return "NO"
	# If sean leaves the smallest piece for his brother, all other pieces
	# will have the same patrickSum as that one lone piece
	return sum(values) - min(values)

if __name__ == "__main__":
	caseCount = input()
	i = 0
	outputs = []
	while i < caseCount:
		candyCount = input()
		candies = map(int, raw_input().split(' '))
		outputs.append(solve(candyCount, candies))
		i += 1
	for i, output in enumerate(outputs):
		print "Case #%i: %s" % (i + 1, str(output))
