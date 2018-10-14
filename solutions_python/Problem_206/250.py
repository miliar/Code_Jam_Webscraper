def solve(D,N,K,S):
	v = 0
	for i in xrange(N):
		t = (D-K[i])/float(S[i])
		if v < t: v = t
	return D/v

testcase = input()
for i in range(testcase):
	D,N = map(int,raw_input().split())
	K,S = [0]*N, [0]*N
	for j in xrange(N): K[j],S[j] = map(int,raw_input().split())
	print "Case #"+str(i+1)+":",solve(D,N,K,S)
