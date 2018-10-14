import sys

def scores(N, K):
	max_score = None
	min_score = None

	diffs = []
	ns = sorted(N)
	ks = sorted(K)
	width = len(ks)
	for i in range(width):
		diff = []
		for j, k in enumerate(ks):
			diff.append(ns[(j+i)%width]-k)
		diffs.append(diff)
		kscore = len(filter(lambda x: x < 0, diff))
		if max_score is None:
			max_score = width - kscore
		else:
			max_score = max(max_score, width - kscore)
		if min_score is None:
			min_score = width - kscore
		else:
			min_score = min(min_score, width - kscore)
	return max_score, min_score

def solve(N, K):
	return "{0} {1}".format(*scores(N, K))

if __name__ == '__main__':
	T = int(sys.stdin.readline())
	for i in xrange(T):
		n = sys.stdin.readline()
		N = map(float, sys.stdin.readline().split(' '))
		K = map(float, sys.stdin.readline().split(' '))
		print "Case #{0}: {1}".format(i + 1, solve(N, K))	