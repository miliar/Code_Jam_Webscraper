# -*- coding: utf-8 -*-
def load_input():
	t = int(raw_input())
	p = []

	for k in xrange(int(t)):
		r, c = map(int, raw_input().split(' '))
		cake = []
		for i in xrange(int(r)):
			l = raw_input()
			cake.append(list(l))
		p.append({'r': r, 'c': c, 'cake': cake})

	return (t, p)

def printcake(r, c, cake):
	for i in xrange(r):
		print ''.join(cake[i])


def solve(p):
	r, c, cake = (p['r'], p['c'], p['cake'])
	used = set([])
	for i in xrange(int(r)):
		for j in xrange(int(c)):
			if cake[i][j] != '?':
				initial = cake[i][j]
				if initial in used:
					continue
				pl = j - 1
				while pl >= 0:
					if cake[i][pl] == '?':
						cake[i][pl] = initial
					else:
						break
					pl -= 1
				pl += 1

				pr = j + 1
				while pr < c:
					if cake[i][pr] == '?':
						cake[i][pr] = initial
					else:
						break
					pr += 1
				pr -= 1

				pu = i - 1
				while pu >= 0:
					if all([True if cake[pu][x] == '?' else False for x in xrange(pl, pr+1)]):
						for x in xrange(pl, pr+1):
							cake[pu][x] = initial
					else:
						break
					pu -= 1

				pd = i + 1
				while pd < r:
					if all([True if cake[pd][x] == '?' else False for x in xrange(pl, pr+1)]):
						for x in xrange(pl, pr+1):
							cake[pd][x] = initial
					else:
						break
					pd += 1
				used.add(initial)
	printcake(r, c, cake) 


def main():
	t, p = load_input()
	for i in xrange(t):
		print 'Case #%d:' % (i + 1)
		solve(p[i])


if __name__ == '__main__':
	main()
