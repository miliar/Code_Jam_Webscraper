def solve(R,C,g):
	initials = []
	qs = []
	for y in xrange(R):
		for x in xrange(C):
			if "?" != g[y][x]:
				initials.append((x,y,g[y][x],1,1))
			else:
				qs.append((x,y))
	for q in qs:
		if g[q[1]][q[0]] != "?":
			continue
		for ii in xrange(len(initials)):
			i = initials[ii]
			newx = min(q[0],i[0])
			newy = min(q[1],i[1])
			neww = max(i[0] - q[0] + i[3],i[3],q[0] - i[0] + 1)
			newh = max(i[1] - q[1] + i[4],i[4],q[1] - i[1] + 1)
			newinitial = (min(q[0],i[0]),min(q[1],i[1]),g[i[1]][i[0]],neww,newh)
			valid = True
			for y in xrange(newinitial[1],newinitial[1]+newinitial[4]):
				for x in xrange(newinitial[0],newinitial[0]+newinitial[3]):
					if not (g[y][x] == "?" or i[2] == g[y][x]):
						valid = False
						break
			if valid:
				for y in xrange(newinitial[1],newinitial[1]+newinitial[4]):
					for x in xrange(newinitial[0],newinitial[0]+newinitial[3]):
						g[y][x] = i[2]
				initials[ii] = newinitial
				break
	return g

if __name__ == "__main__":
	t = int(raw_input())
	for i in xrange(1, t + 1):
		r,c = [int(s) for s in raw_input().split(" ")]
		g = []
		for j in xrange(r):
			row = [list(s) for s in raw_input().split(" ")][0]
			g.append(row)
		answer = solve(r,c,g)
		print "Case #" + str(i) + ":"
		for k in answer:
			print "".join(k)
