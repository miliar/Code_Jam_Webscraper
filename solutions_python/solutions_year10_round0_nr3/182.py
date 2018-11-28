import sys

lines = sys.stdin.readlines()

C = int(lines[0])
for c in range(C):
	(R, k, N) = (int(x) for x in lines[2*c+1].split())
	g = [int(x) for x in lines[2*c+2].split()]

	EU = 0	

	for r in range(R):
		left = k
		eu = 0
		while (left >= g[eu]):
			left -= g[eu]
			eu += 1
			if eu >= len(g): break
		EU += (k-left)
		x = g[eu:] + g[:eu] 		
		g = x

	print "Case #%d: %ld" % (c+1, EU)
	
