from sys import stdin


T = int(stdin.readline())

for case in range(1,T+1):
	r, t = map(int, stdin.readline().split())

	remainingPaint = t
	nRings = 0
	while remainingPaint > 0:
		# paintNeeded = (r+(nRings*2+1))**2 - (r+(nRings*2))**2
		paintNeeded = 2*r + 4*nRings + 1
		if remainingPaint >= paintNeeded:
			remainingPaint -= paintNeeded
			nRings += 1
		else:
			break

	print "Case #%d: %d" % (case, nRings)
