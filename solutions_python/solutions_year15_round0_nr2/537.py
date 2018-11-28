def solve():
	d = int(raw_input())
	a = map(int, raw_input().split())
	res = 1000000
	for m in xrange(1, 1001):
		p = 0
		for x in a:
			p += (x - 1) / m
		res = min(res, m + p)
	return res
			

for i in xrange(input()):
	print "Case #%d: %d" % (i + 1, solve())
