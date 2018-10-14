#!/usr/bin/python

for i in xrange(int(raw_input().strip())):
	tokens = [int(x) for x in raw_input().strip().split(" ")]
	N = tokens[0]
	S = tokens[1]
	p = tokens[2]
	
	ans = 0
	
	for t in tokens[3:]:
		if t % 3 == 0:
			mn = t / 3
		else:
			mn = t / 3 + 1
		if mn >= p:
			ans += 1
		elif S:
			if t % 3 == 2 and (t / 3) + 2 >= p:
				ans += 1
				S -= 1
			elif t > 1 and (t / 3) + 1 >= p:
				ans += 1
				S -= 1
	print "Case #%d: %d" % (i+1, ans)
