import sys

def tiles(m):
	r = len(m)
	c = len(m[0])
	i = 0
	while i < r:
		j = 0
		while j < c:
			if m[i][j] == '#':
				if i+1<r and j+1<c and m[i][j+1]=='#' and m[i+1][j]=='#' and m[i+1][j+1]=='#':
					m[i][j] = '/'
					m[i][j+1] = '\\'
					m[i+1][j] = '\\'
					m[i+1][j+1] = '/'
				else:
					return (False, m)
			j += 1
		i += 1
	return (True, m)

if __name__ == '__main__':
	t = int(sys.stdin.readline())
	i = 1
	while i <= t:
		l = sys.stdin.readline().split()
		r = int(l[0])
		c = int(l[1])
		m = []
		j = 0
		while j < r:
			m.append(list(sys.stdin.readline().rstrip()))
			j += 1
		ret = tiles(m)
		print 'Case #%d:' % (i)
		if ret[0]:
			for x in ret[1]:
				s = ''
				for y in x:
					s += y
				print s
		else:
			print 'Impossible'
		i += 1
