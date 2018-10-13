from collections import defaultdict

def nodes_trie(S):
	dc = {}
	nodes = 1
	for s in S:
		cdic = dc
		for c in s:
			if c not in cdic:
				nodes += 1
				cdic[c] = {}
			cdic = cdic[c]
	return nodes

def solve(S, N):
	mx = 0
	ct = defaultdict(int)
	for d in xrange(N**len(S)):
		servers = [[] for i in xrange(N)]
		num = d
		for s in S:
			servers[num%N].append(s)
			num /= N
		if all(servers):
			x = sum(map(nodes_trie, servers))
			if x == mx:
				ct[x] += 1
			elif x > mx:
				ct[x] += 1
				mx = x
	return mx, ct[mx]



T = int(raw_input())
for test in xrange(1,T+1):
	M, N = map(int, raw_input().split())
	S = []
	for i in xrange(M):
		S.append(raw_input())
	print "Case #" + str(test) + ": " + " ".join(map(str, solve(S, N)))