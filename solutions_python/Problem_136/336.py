import sys

TT = int(sys.stdin.readline())

for T in xrange(1,TT+1):
	C, F, X = map(float, sys.stdin.readline().split())
	rate = 2
	tBuild = 0
	ans = X / rate
	while True:
		build = C / rate
		wait = X / (rate+F)
		if tBuild + build + wait >= ans: break
		ans = tBuild + build + wait
		rate += F
		tBuild += build

	print "Case #%d: %.7f" % (T, ans)


