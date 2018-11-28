import sys
#sys.stdin = open ('C-small.in')
#sys.stdout = open ('C-small.out', 'w')

T = input ()
for i in xrange (T):
	n = input ()
	c = map (int, raw_input ().split ())
	if reduce (lambda x, y: x ^ y, c, 0) != 0:  
		print 'Case #{}: NO'.format (i + 1)
	else:
		print 'Case #{}: {}'.format (i + 1, sum (c) - min (c))
		
