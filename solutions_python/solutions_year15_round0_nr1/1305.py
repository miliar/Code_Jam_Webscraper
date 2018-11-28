T = int(raw_input())

for i in xrange(1, T+1):
	(mx, shy) = raw_input().split()
	mx = int(mx)

	shymap = {}
	for j in xrange(mx + 1):
		shymap[j] = int(shy[j])

	extra, total = 0, shymap[0]
	for j in xrange(1, mx + 1):
		extraCurLevel = 0
		if j > total:
			extraCurLevel = j - total
			extra += extraCurLevel

		total += shymap[j] + extraCurLevel

	print 'Case #' + str(i) + ': ' + str(extra)