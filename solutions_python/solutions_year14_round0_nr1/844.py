t = int(raw_input());

for cs in xrange(t):
	s = []
	
	for j in range(2):
		a = int(raw_input())
		for i in xrange(4):
			u = set(map(int,raw_input().split()))
			if i+1 == a:
				s.append(u)
	n = s[0].intersection(s[1])
	l = len(n)
	if l == 1:
		ans = n.pop()
	elif l == 0:
		ans = "Volunteer cheated!"
	else:
		ans = "Bad magician!"

	print "Case #%d: %s" % (cs+1, ans)
	
