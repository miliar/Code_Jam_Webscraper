#!/usr/bin/python

if __name__ == '__main__': 
	n = int(input())
	for tt in xrange(n):
		print 'Case', '#%i:' % (tt + 1),

		add = 0
		m, l = raw_input().split()
		i = 0
		s = 0
		for c in l:
			if c != '0':
				if s < i:
					add += i - s
					s = i
				s += int(c)
			i += 1

		print add