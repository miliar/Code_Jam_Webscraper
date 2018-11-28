for cc in xrange(1, input() + 1):
	N, V, X = raw_input().split()
	N = int(N)
	V = float(V)
	X = float(X)
	D = []
	for _ in xrange(N):
		D.append(map(float, raw_input().split())[::-1])
	ans = 123456789012345678901234567890
	leftr = 0
	leftt = 0
	rightr = 0
	rightt = 0
	midr = 0
	for i in xrange(N):
		if D[i][0] < X:
			leftr += D[i][1]
			leftt += D[i][0] * D[i][1]
		if D[i][0] == X:
			midr += D[i][1]
		if D[i][0] > X:
			rightr += D[i][1]
			rightt += D[i][0] * D[i][1]
	if leftr > 0:
		leftt /= leftr
	if rightr > 0:
		rightt /= rightr
	if midr == 0 and (leftr == 0 or rightr == 0):
		print "Case #" + str(cc) + ": IMPOSSIBLE"
	else:
		den = 1.0
		if leftr and rightr:
			den += (X - rightt)/(leftt - X) + (midr/rightt)
			x2 = V/den
			x1 = x2 * (X - rightt)/(leftt - X)
			ans = 0
			if leftr:
				ans = max(ans, x1/leftr)
			if rightr:
				ans = max(ans, x2/rightr)
			if midr:
				ans = max(ans, (V - (x1 + x2))/midr)
		else:
			ans = V/midr
		print "Case #" + str(cc) + ": %.10f" % (ans)

