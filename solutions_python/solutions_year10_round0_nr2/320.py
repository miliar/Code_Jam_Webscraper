# -*- coding: utf-8 -*-
def gcd(a,b):

	while(b):
		a, b = b, a%b

	return a

maxcases = int(raw_input())

for ncase in xrange(maxcases):

	line = raw_input().split(' ')

	n = int(line[0])
	a = int(line[1])
	d = abs(int(line[2]) - a);

	for i in line[ 3: ]:
		d = gcd( d, abs(int(i) - a) )

	sol = (((-a) % d) + d) % d

	print 'Case #' + str(ncase+1) + ': ' + str(sol)