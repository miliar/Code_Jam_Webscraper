from sys import stdin
readline = stdin.readline

T = int(readline())
for t in xrange(1, T+1):
	D, N = map(int, readline().strip().split())
	tmin = 0
	for i in xrange(N):
		K, S = map(float, readline().strip().split())
		try:
			tmin = max(tmin, (D-K)/S)
		except:
			pass
	
	ans = D/tmin
	
	print "Case #%d: %.8f" % (t, ans)
