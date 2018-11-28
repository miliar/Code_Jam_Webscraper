def solve(c):
	ini = None
	validRow = False
	changed = False
	for i, r in enumerate(c):
		ini = None
		for j, p in enumerate(r):
			if p != '?':
				validRow = True
				ini = p
				k = j-1
				while k >= 0 and c[i][k] == '?':
					c[i][k] = ini
					k-=1
			elif ini is not None:
				c[i][j] = ini
		if validRow and not changed:
			changed = True
			for j in range(len(r)):
				for k in range(i):
					c[k][j] = c[i][j]
		if ini is None:
			if validRow:
				for j in range(len(r)):
					c[i][j] = c[i-1][j]
		# print(c)
	ret = ""
	for r in c:
		ret+=''.join(r)
		ret+='\n'
	return ret[:-1]

if __name__ == '__main__':
	fname = 'A-large.in'
	oname = 'p1.out'
	f = open(fname, 'r')
	g = open(oname, 'w+')
	first = True
	case = 1
	cake = []
	for line in f:
		ans = "IMPOSSIBLE"
		if first: 
			first = False
		else:
			strs = line.split(' ')
			print(strs)
			if len(strs) > 1:
				if len(cake) == 0: continue
				a = solve(cake)
				if a is not None: ans = a
				g.write("Case #{0}: \n{1}\n".format(str(case), str(ans)))
				case+=1
				cake = []
			else:
				if line[-1] == '\n': cake+=[list(line[:-1])]
				else: cake+=[list(line)]
	a = solve(cake)
	g.write("Case #{0}: \n{1}\n".format(str(case), a))
	case+=1