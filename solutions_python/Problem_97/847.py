T = int(raw_input())
for t in range(1, T+1):
	A, B = map(int, raw_input().split())
	recycled = 0
	for n in range(A, B+1):
		s = str(n)
		if len(s) > 1:
			added = []
			for i in range(1, len(s)):
				m = int(s[i:] + s[:i])
				if n < m <= B and not m in added:
					recycled += 1
					added.append(m)
	print "Case #{0}: {1}".format(t, recycled)
