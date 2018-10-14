T = int(raw_input())
for i in range(T):
	R, k, N = map(int, raw_input().split())
	g = map(int, raw_input().split())
	total = 0
	rc = []
	for j in range(R):
		for l in range(N):
			if sum(rc)+g[0] <= k:
				g0 = g.pop(0)
				rc.append(g0)
			else:
				break
		total += sum(rc)
		g.extend(rc)
		rc = []
	print "Case #{0}: {1}".format(i+1, total)
