def testCase():
	data = [int(n) for n in raw_input().split()]
	L, t, N, C = data[:4]
	a = data[4:4+C]
	assert len(a) == C

	n = N // C
	rem = a[:N-n*C]
	distances = n*a + rem
	assert N == len(distances)

	time_bonus = [0] * len(distances)
	t1 = 0
	for i, dist in enumerate(distances):
		t2 = t1 + dist*2
		if t1 >= t:
			time_bonus[i] = dist
		elif t <= t2:
			time_bonus[i] = (t2 - t) // 2
		t1 = t2

	if not L:
		return t1
	return t1 - sum(sorted(time_bonus)[-L:])

if __name__ == '__main__':
	for i in xrange(int(raw_input())):
		print "Case #%d: %d" % (i+1, testCase())
