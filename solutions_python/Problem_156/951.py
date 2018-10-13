"""
f = open('/home/nikita/cj/A-large.in', 'r')
tests = int(f.readline())
for t in range(0, tests):
	line = f.readline().split()
	g = int(line[0])
	s = line[1]
	guests = 0
	clapping = int(s[0])
	for i in range(1, len(s)):
	        if (clapping < i):
			guests = guests + (i - clapping)
			clapping = i
		clapping = clapping + int(s[i])
	print "Case #"+str(t+1) +": " + str(guests)
"""
v = {1 : 1, 2 : 1, 3 : 1, 4 :2, 5 : 2, 6 : 2, 7 : 2, 8 : 2, 9 : 3}
d = []

def try_calc(steps_guaranteed, specials, i):
	if (len(d) == i):
		return (steps_guaranteed, specials)
	if (d[i] <= steps_guaranteed):
		return try_calc(steps_guaranteed, specials, i + 1)
	elif (v[d[i]] == 1):
		return try_calc(d[i], specials, i + 1)
	else:
		g1, s1 = try_calc(d[i], specials, i + 1)
		#print g1, s1
		g2, s2 = try_calc(max(d[i]/2 + d[i]%2, steps_guaranteed), specials+1, i+1)
		cg = g2
		cs = s2
		if (g1 + s1 <= g2 + s2):
			cg = g1
			cs = s1
		if (d[i] == 9):
			g3, s3 = try_calc(max(d[i]/3, steps_guaranteed), specials + 2, i+1)
			if (g3 + s3 < cs + cg):
				cs = s3
				cg = g3
		return (cg, cs)
			


f = open('/home/nikita/cj/B-small-attempt2.in', 'r')
tests = int(f.readline())
for t in range(0, tests):
	dn = int(f.readline())
	d = sorted(map(int, f.readline().split()), reverse=True)
	g1, s1 = try_calc(0, 0, 0)
	resu  = g1 + s1
	print "Case #"+str(t+1) +": " + str(resu)
	
