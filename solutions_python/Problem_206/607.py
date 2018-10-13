import sys

T = int(sys.stdin.readline())

for k in xrange(T):
	D,N = map(int, sys.stdin.readline()[:-1].split(" "))
	KS = []
	for i in xrange(N):
		Ki, Si = map(int, sys.stdin.readline()[:-1].split(" "))
		KS.append((Ki,Si))


	times = []
	for Ki,Si in KS:
		t = (1.0 * (D - Ki)) / Si
		times.append(t)

	t = max(times)

	
	print "Case #{}: {:.6f}".format(k+1, (D * 1.0) / t)
	
