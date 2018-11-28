T = input()

for i in xrange(T):
	p1 = []
	p2 = []
	a = input()
	for _ in xrange(4):
		p1.append(map(int, raw_input().split()))
	b = input()
	for _ in xrange(4):
		p2.append(map(int, raw_input().split()))
	ans = [x for x in p1[a-1] if x in p2[b-1]]
	if len(ans) == 1:
		print "Case #%d: %d" % (i+1, ans[0])
	elif len(ans) == 0:
		print "Case #%d: Volunteer cheated!" % (i+1)
	else:
		print "Case #%d: Bad magician!" % (i+1)
