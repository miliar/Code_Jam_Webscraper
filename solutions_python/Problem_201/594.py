def solve(L):
	N,K = L[0],L[1]-1
	t = 0
	while K>=2**(t+1)-1: t+=1
	s = N-2**t+1
	v = s/2**t
	r = s-v*2**t
	k = K-2**t+2
	return v if k>r else v+1
testcase = input()
for i in range(testcase):
    N = solve(map(int,raw_input().split()))
    print "Case #"+str(i+1)+":",N/2,(N-1)/2
