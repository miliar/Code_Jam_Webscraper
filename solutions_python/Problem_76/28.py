def readint(): return int(raw_input())

T = readint()
for t in xrange(T):
	N = int(raw_input())
	res = 0
	sum = 0
	min = 1000000
	for i in raw_input().split():
		r = int(i)
		res ^= r
		sum += r
		if min > r: min = r
	if res == 0:
		sum -= min
		print "Case #%d: %s" % (t + 1, sum)
	else:
		print "Case #%d: NO" % (t + 1)