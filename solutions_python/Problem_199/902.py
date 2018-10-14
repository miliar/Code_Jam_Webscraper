from collections import deque

def printb(v, N):
	s = ""
	for n in xrange(N):
		if (v & 1):
			s = "-" + s
		else:
			s = "+" + s
		v = v >> 1
	print s, len(s)

def solve():
	[S, K] = raw_input().split()
	K = int(K)
	F = 0
	for k in xrange(K):
		F = (F << 1 )+ 1
	b = lambda x: printb(x, len(S))
	v = 0
	C = len(S) - K + 1

	for s in S:
		v = (v << 1) + (s == '-')

	IMP = 10000

	memo = {}

	# def swap(v, steps):
	# 	if v == 0: # we are done!
	# 		return steps

	# 	memo[v] = steps

	# 	minv = IMP

	# 	for shift in xrange(C):
	# 		newv = v ^ (F << shift)
	# 		if newv in memo:
	# 			if memo[newv] <= steps:
	# 				continue # no point of continuing it
	# 		minv = min(swap(newv, steps+1), minv)

	# 	return minv

	# ans = swap(v, 0)

	wl = deque([])
	wl.append((v,0))

	while len(wl) > 0:
		(v, steps) = wl.popleft()
		if steps > IMP:
			return "IMPOSSIBLE"
		if v == 0: # we are done!
			return steps

		memo[v] = steps

		for shift in xrange(C):
			newv = v ^ (F << shift)
			if newv in memo: continue
			wl.append((newv,steps+1))

	return "IMPOSSIBLE"

##########################################

T = int(raw_input())

for t in xrange(T):
	ans = solve()
	print "Case #%d:"%(t+1), ans
