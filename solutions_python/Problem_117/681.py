import fileinput
from itertools import izip

def readline(inp):
	return map(int, inp.readline().strip().split(' '))

def validate(a):
	rowmaxs = map(max, a)
	colmaxs = map(max, izip(*a))
	for row, rowmax in izip(a, rowmaxs):
		for val, colmax in izip(row, colmaxs):
			if not (val == rowmax or val == colmax):
				return 'NO'
	return 'YES'

inp = fileinput.input() 
(t,) = readline(inp)
for i in xrange(1,t+1):
	(n, m) = readline(inp)
	a = []
	for _ in xrange(n):
		a.append(readline(inp))
	print 'Case #{0}: {1}'.format(i, validate(a))
inp.close()