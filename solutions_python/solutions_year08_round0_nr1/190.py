import sys

T = int(raw_input())
for i in range(0,T):
	S = int(raw_input())
	dic = {}
	for j in range(0,S):
		p = sys.stdin.readline().strip()
		dic[p] = j
	Q = int(raw_input())
	seen,ans = {},0
	for j in range(0,Q):
		p = sys.stdin.readline().strip()
		try:
			if seen[p] == 1:
				continue
		except KeyError:
			seen[p] = 1
		if len(seen) == S:
			seen =  {}
			seen[p] = 1
			ans += 1
	print "Case #%d: %d" % (i+1,ans)
