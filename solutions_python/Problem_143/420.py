def Check(a, b, k):
	nOptions = 0

	for i in xrange(a):
		for j in xrange(b):
			if i & j < k:
				nOptions += 1
				
	return nOptions
	
nTestCases = int(raw_input())
for i in xrange(nTestCases):
	lValues = [int(x) for x in raw_input().split()]
	print "Case #%d: %d" % (i + 1, Check(lValues[0], lValues[1], lValues[2]))