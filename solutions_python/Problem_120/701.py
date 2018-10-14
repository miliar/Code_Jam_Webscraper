def case(n):
	r, t = map(int, raw_input().split(' '))
	used = 0
	i = 0
	while True:
		used += 2*r + 4*i + 1
		if used > t:
			break
		i += 1
	print 'Case #%d: %d' % (n, i)

if __name__ == '__main__':
	for i in xrange(int(raw_input())):
		case(i + 1)