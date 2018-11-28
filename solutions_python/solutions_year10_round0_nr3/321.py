f = open("C-large.in", "r")
c = -1

for line in f:
	c += 1
	if c == 0:
		continue
	
	g = line.split(" ")
	
	if c % 2 == 1:
		R = int(g[0])
		k = int(g[1])
		N = int(g[2])
		continue
	
	g = map(int, g)
	oldr = []
	oldm = []
	for gi in g:
		oldr += [0]
		oldm += [0]
	
	
	i = 0
	j = 0
	r = 1
	m = 0
	while r <= R:
		if oldr[i] == 0:
			oldr[i] = r
			oldm[i] = m
		else:
			m += (R - r + 1) / (r - oldr[i]) * (m - oldm[i])
			r += ((R - r + 1) / (r - oldr[i])) * (r - oldr[i])
			if r > R:
				continue
		
		s = 0
		j = i
		while s + g[i] <= k:
			s += g[i]
			i += 1
			if i == len(g):
				i = 0
			if i == j:
				break
		m += s
		r += 1
	
	print "Case #%d: %d" % (c / 2, m)

f.close()