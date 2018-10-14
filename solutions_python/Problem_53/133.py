TESTCASES = int(raw_input())

for CASE in range(TESTCASES):
	(N,K) = map(int, raw_input().split(' '))

	#print "K=",K,'and N=',N,'-- 2^N-1=',2**(N-1)

	s = K & (2**(N-1))
	while N > 1:
		N = N-1
		if s: s = K & (2**(N-1))

	print "Case #%d: %s" % (CASE+1, s and "ON" or "OFF")
