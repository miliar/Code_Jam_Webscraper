def solve(D, N, horses):
	t = [(D - h[0])/h[1] for h in horses]
	return D / max(t)



T = int(raw_input())
for case in xrange(1, T+1):
	D, N = map(float, raw_input().split())
	horses = [map(float, raw_input().split()) for _ in xrange(int(N))]
	solution = solve(D, int(N), horses)
	print "Case #{}: {}".format(case, solution)


