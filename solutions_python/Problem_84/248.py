def solve(s):
	if '#' in s:
		k = s.split('\n')
		p1 = 0
		for l1 in range(len(k)):
			if k[l1].find('#') != -1:
				p1 = k[l1].find('#')
				break
		if l1 == len(k)-1 or p1 == len(k[0])-1:
			return False
		if k[l1][p1+1] == k[l1+1][p1] == k[l1+1][p1+1] == '#':
			k[l1] = k[l1][:p1] + '/' + k[l1][p1+1:]
			k[l1]= k[l1][:p1+1] + '\\' + k[l1][p1+2:]
			k[l1+1] = k[l1+1][:p1] + '\\' + k[l1+1][p1+1:]
			k[l1+1] = k[l1+1][:p1+1] + '/' + k[l1+1][p1+2:]
			return solve("\n".join(k))
		else:
			return False
	else:
		return s

def solveinput(s):
	s = '\n'.join(s.split('\n')[1:])
	i = 1
	while s:
		k = s.split('\n')
		r, c = map(int,k[0].split(' '))
		g = k[1:1+r]
		l = solve('\n'.join(g))
		print "Case #%d:" % i
		print 'Impossible' if l is False else l
		s = '\n'.join(k[1+r:])
		i += 1
