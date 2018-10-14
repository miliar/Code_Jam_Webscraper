t = int(raw_input())
sol = []

for i in xrange(t):
	x,r,c = [int(z) for z in raw_input().split()]
	mi = min(r,c)
	ma = max(r,c)
	a = r*c
	g = True
	if a%x != 0:
		g = False
	else:
		if x == 2:
			g = True
		elif x == 3:
			if mi < 2:
				g = False
			else:
				g = True
		elif x == 4:
			if mi < 3:
				g = False
			else:
				g = True
		elif x == 5:
			if mi < 3:
				g = False
			elif mi == 3:
				if ma < 10:
					g = False
				else:
					g = True
			else:
				g = True
		elif x == 6:
			if mi < 4:
				g = False
			else:
				g = True
		else:
			g = True
	if g:
		sol.append("Case #" + str(i+1) + ": GABRIEL")
	else:
		sol.append("Case #" + str(i+1) + ": RICHARD")

for line in sol:
	print line