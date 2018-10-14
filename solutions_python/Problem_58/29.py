#!/usr/bin/python

def check(a, b):
	steps = 0
	while True:
		if (a == b):
			return (steps+1)%2
		if (a > 2*b) or (b > 2*a):
			return steps%2
		if (a > b):
			a -= b
		else:
			b -= a
			
		steps += 1
			

T = int(raw_input())
for t in xrange(T):
	a1, a2, b1, b2 = tuple([int(item) for item in raw_input().split()])

	ans = 0
	for i in xrange(a1, a2+1):
		for j in xrange(b1, b2+1):
			if check(i,j) == 0:
				#print i, j
				ans += 1
	
	print "Case #%d:" % (t+1),
	print ans