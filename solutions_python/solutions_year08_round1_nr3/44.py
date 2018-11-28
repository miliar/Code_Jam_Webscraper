#!/usr/bin/python
# Thomas Karpiniec

# Using the high precision math library mpath http://code.google.com/p/mpmath/
from mpmath import *
mp.dps = 100

num_cases = int(raw_input())

for case in xrange(1,num_cases+1):
	n = int(raw_input())
	
	ans = mpf(0)
	
	num_terms = n + 1
	a = [1, 1]
	b = []
	for i in xrange(num_terms - 2):
		b = []
		a.insert(0, 1)
		a.append(1)
		#print a
		for j in xrange(len(a) - 1):
			b.append(a[j] + a[j+1])
		b[0] = 1
		b[len(b)-1] = 1
		a = b
		#print a
	#print n
	#print num_terms
	#print a
	
	# Now have binomial tree
	for i in xrange(num_terms):
		#print "n is %d i is %d" % (n, i)
		term = (mpf(3) ** mpf(i)) * (sqrt(5) ** mpf(n - i)) * mpf(a[i])
		ans += term
		#print "term of %s brings ans to %s" % (term, ans)
	
	ans = floor(ans)
	ans = ans % 1000
	print "Case #%d: %03d" % (case, ans)