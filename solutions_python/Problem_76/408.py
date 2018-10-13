import itertools

def xor_sum(l):
	return reduce(lambda x,y:x^y, l)

def solve_test_case(infile):
	N = int(infile.readline().rstrip())
	candies = [int(candy) for candy in infile.readline().rstrip().split(' ')]
	assert N == len(candies)
	# Patrick uses XOR instead of plus.
	# "Patrick-equal-division" is possible if XOR of all candies is 0
	if xor_sum(candies) != 0:
		return "NO"
	candies.sort()
	return str(sum(candies[1:]))

def solve(filename):
	infile = open(filename, 'rb')
	T = infile.readline()
	for i in xrange(int(T)):
		result = solve_test_case(infile)
		print "Case #%d: %s" % (i+1, result)

if __name__ == "__main__":
	import sys
	solve(sys.argv[1])