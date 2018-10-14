import codecs
with codecs.open("C-large.in", "r", "utf- 8") as f:
	temp = f.readlines()
	c = 0
	for x in temp[1:]:
		t = x.strip().split()
		if len(t) <= 1:
			continue
		c += 1
		x = 0
		t = [int(z) for z in t]
		t.sort()
		s = 0
		for y in t[1:]:
			x ^= y
			s += y
		if x != t[0]:
			print "Case #{0}: NO".format(c)
		else:
			print "Case #{0}: {1}".format(c, s)
