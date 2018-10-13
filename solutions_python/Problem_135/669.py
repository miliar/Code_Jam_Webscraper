t=int(raw_input())
for x in xrange(t):
	a = int(raw_input())
	m=[[int(i) for i in raw_input().split()] for j in xrange(4)]
	l1 = set(m[a-1])
	a = int(raw_input())
	m=[[int(i) for i in raw_input().split()] for j in xrange(4)]
	l2 = set(m[a-1])
	print "Case #%s:"%(x+1),
	if len(l1&l2) == 1:
		print list(l1&l2)[0]
	elif len(l1&l2) == 0:
		print "Volunteer cheated!"
	else:
		print "Bad magician!"