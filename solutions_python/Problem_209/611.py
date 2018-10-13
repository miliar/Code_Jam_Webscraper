t = input()
from collections import defaultdict
def solve(pancakes, n, k, dp):
	# print "calling for {0}, {1}".format(n, k)
	if ((n, k)) in dp:
		# print 'returning {0} for {1}, {2}'.format(dp[(n, k)], n, k)
		return dp[(n, k)]

	if n == 0:
		# print 'returning {0} for {1}, {2}'.format(0, n, k)
		return 0

	if k < 0:
		# print 'returning {0} for {1}, {2}'.format(9876543211111111, n, k)
		return -9876543211111111

	if n == 1:
		p = pancakes[k]
		dp[(n, k)] = p[0]**2 + 2*p[0]*p[1]
		# print p[0]**2 + 2*p[0]*p[1]
		# print 'returning {0} for {1}, {2}'.format(p[0]**2 + p[0]*p[1], n, k)
		return p[0]**2 + 2*p[0]*p[1]

	max_ = -1
	for cand in xrange(0, k):
		max_ = max(max_, solve(pancakes, n-1, cand, dp))

	p = pancakes[k]
	dp[(n, k)] = max_ + 2*p[0]*p[1]
	# print 'returning {0} for {1}, {2}'.format(dp[(n, k)], n, k)
	return dp[(n, k)]

for idx in xrange(1, t + 1):

	n, k = map(int, raw_input().split())

	pancakes = []

	for _ in xrange(n):
		a, b = map(int, raw_input().split())
		pancakes.append((a, b))
	dp = defaultdict(int)
	pancakes.sort(reverse=True)
	# print pancakes
	best = -1
	for i in xrange(0, n):
		best = max(best, solve(pancakes, k, i, dp))

	print "Case #{0}: ".format(idx) +  "%.10f" % (best*3.14159265359)
	