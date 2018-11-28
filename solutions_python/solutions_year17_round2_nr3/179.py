def solve(N,Q,E,S,D,U,V):
	P = [D[i][i+1] for i in xrange(N-1)]
	time = [1.e20]*N
	time[0] = 0.
	for i in xrange(1,N):
		for j in xrange(i):
			total = sum(P[j:i])
			if total <= E[j]:
				rest = time[j] + total/float(S[j])
				if rest < time[i]: time[i] = rest
	return [time[-1]]

testcase = input()
for t in range(testcase):
    N,Q = map(int,raw_input().split())
    E,S,D = [0]*N,[0]*N,[]
    for i in xrange(N): E[i],S[i] = map(int,raw_input().split())
    for i in xrange(N): D.append(map(int,raw_input().split()))
    U,V = [0]*Q,[0]*Q
    for i in xrange(Q): U[i],V[i] = map(int,raw_input().split())
    print "Case #"+str(t+1)+":"," ".join(map(str,solve(N,Q,E,S,D,U,V)))
