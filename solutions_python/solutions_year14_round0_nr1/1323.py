
testcase = int(raw_input())
for caseno in xrange(1, testcase + 1):
	a = int(raw_input()) - 1
	l1 = []
	m1 = {}
	for i in xrange(4):
		row = map(int, raw_input().split())
		l1.append(row)
		for n in row:
			m1[n] = i
	b = int(raw_input()) - 1
	l2 = []
	m2 = {}
	for i in xrange(4):
		row = map(int, raw_input().split())
		l2.append(row)
		for n in row:
			m2[n] = i

	t = [[[], [], [], []] for x in xrange(4)]

	for n in xrange(1, 17):
		i, j = m1[n], m2[n]
		t[i][j].append(n)
	if len(t[a][b]) == 0:
		print "Case #%d: Volunteer cheated!" % (caseno)
	elif len(t[a][b]) > 1:
		print "Case #%d: Bad magician!" % (caseno)
	else:
		print "Case #%d: %d" % (caseno, t[a][b][0])
