import sys

T = int(raw_input())

for tc in xrange(1, T + 1):
	N, K = map(int, raw_input().split())

	gaps = dict()

	gaps[N] = 1

	occupied = 0
	while occupied < K:
	    maxGap = max(gaps.keys())
	    numGap = gaps[maxGap]
	    del gaps[maxGap]

	    if maxGap % 2:
		maxAns = minAns = (maxGap - 1) / 2
	    else:
		maxAns = maxGap / 2
		minAns = maxAns - 1

	    if (occupied + numGap) > K:
		break
	    
	    occupied += numGap
	    gaps[maxAns] = gaps.get(maxAns, 0) + numGap
	    gaps[minAns] = gaps.get(minAns, 0) + numGap
	
	print "Case #%d: %d %d" % (tc, maxAns, minAns)
