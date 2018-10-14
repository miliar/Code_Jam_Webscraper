C = int(raw_input())

for c in range (1,C+1):
	(N, K, B, T) = map(int,raw_input().split())
	xis = map(int,raw_input().split())
	vis = map(int,raw_input().split())
	
	atTime = 0
	late = 0
	swapCount = 0
	
	zippedReversed = zip(xis,vis)
	zippedReversed.reverse()
	
	arrivalTimes = []
	for (xi,vi) in zippedReversed:
		t = (B-xi)/float(vi)
		arrivalTimes.append(t)
	for time in arrivalTimes:
		if atTime >= K:
			break
		if time <= T:
			swapCount += late
			atTime += 1
		else:
			late += 1
	if late > N-K:
		print "Case #%d: IMPOSSIBLE" % (c)
	else:
		print "Case #%d: %d" % (c,swapCount)
	