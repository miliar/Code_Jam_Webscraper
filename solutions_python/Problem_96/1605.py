T = (int)(raw_input())
for i in range(T):
	line = raw_input().split()
	d = (int)(line[1])
	p = (int)(line[2])
	w = 0
	for s in line[3:]:
		k = (int)(s)
		if k >= (3*p-2): w += 1
		else:
			if (k >= p and (k == (3*p-3) or k == (3*p-4)) and d > 0):
				w += 1
				d -= 1
	print "Case #%d: %d" % ((i+1), w)

