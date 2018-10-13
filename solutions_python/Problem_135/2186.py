t = int(raw_input())

for i in xrange(t):
	x = int(raw_input())
	xx = []
	for j in range(4):
		xx.append(raw_input().split())
	y = int(raw_input())
	yy = []
	for j in range(4):
		yy.append(raw_input().split())

	r = []
	for j in range(16):
		if j + 1 in [int(s) for s in xx[x - 1]] and j + 1 in [int(s) for s in yy[y - 1]]:
			r.append(j + 1)

	if len(r) == 0:
		print 'Case #%d: Volunteer cheated!' % (i + 1)
	if len(r) == 1:
		print 'Case #%d: %d' % (i + 1, r[0])
	if len(r) > 1:
		print 'Case #%d: Bad magician!' % (i + 1)