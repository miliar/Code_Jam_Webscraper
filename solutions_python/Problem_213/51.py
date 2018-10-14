getline = lambda: [int(x) for x in raw_input().split()]

from collections import Counter

T = int(raw_input())
for test_case in range(T):
	N, C, M = getline()
	tickets = [getline() for _ in range(M)]
	ranks = Counter(u for [u,v] in tickets)
	individuals = Counter(v for [u,v] in tickets)
	ticket = {0:0}
	for rank in range(1,N+1):
		ticket[rank] = ticket[rank-1]
		if rank in ranks:
			ticket[rank] += ranks[rank]
	answer = 0
	R = max(ticket[x]/x for x in range(1,N+1))
	I = max(individuals.values())
	Y = max(R,I)
	Z = sum(max(0, ranks[x]-Y) for x in range(1,N+1))
	print "Case #%s: %s %s"%(test_case+1, Y, Z)
