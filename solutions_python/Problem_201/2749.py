def choose_stall(occupied):
	occupied = sorted(occupied)

	poss = []
	for i in xrange(1, len(occupied)):
		if occupied[i - 1] == occupied[i]:
			continue
		pair = [occupied[i - 1], occupied[i]]

		p1 = (pair[0] + pair[1]) / 2
		poss.append([p1, p1 - pair[0], pair[1] - p1])

		if p1 * 10 != int(10. * (pair[0] + pair[1]) / 2.):
			p2 = p1 + 1
			poss.append([p2, p2 - pair[0], pair[1] - p2])

	if len(poss) == 1:
		return poss[0][0]

	minlr = sorted(poss, key=lambda x:min(x[1], x[2]), reverse=True)

	#maxlr_val = max(maxlr[0][1], maxlr[0][2])
	#minlr_val = min(minlr[0][1], minlr[0][2])

	#print minlr

	if min(minlr[0][1], minlr[0][2]) > min(minlr[1][1], minlr[1][2]):
		return minlr[0][0]

	maxlr = sorted([p for p in poss if min(p[1], p[2]) == min(minlr[0][1], minlr[0][2])], key=lambda x:max(x[1], x[2]), reverse=True)
	#print maxlr
	if max(maxlr[0][1], maxlr[0][2]) > max(maxlr[1][1], maxlr[1][2]):
		return maxlr[0][0]

	end = sorted([p for p in maxlr if max(p[1],p[2])==max(maxlr[0][1], maxlr[0][2])], key=lambda x:x[0])

	return end[0][0]


T = input()
for t in xrange(1, T+1):
	N, K = raw_input().split()

	size = int(N)

	occupied = [0, size+1]

	for i in xrange(1, int(K) + 1):
		c = choose_stall(occupied)
		#print a, b, c
		occupied.append(c)
		#print occupied

	occupied = sorted(occupied)

	for i in xrange(len(occupied)):
		if occupied[i] == c:
			l = c - occupied[i - 1] - 1
			r = occupied[i + 1] - c - 1
			b = max(l, r)
			a = min(l, r)

	print "Case #%d: %d %d" % (t, b, a)










