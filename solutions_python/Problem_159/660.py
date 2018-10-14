import os, sys

def solve( N, m ) :
	n1 = 0
	rate = 0
	for i in xrange(N-1) :
		a, b = m[i], m[i+1]
		k = max( a-b, 0 )
		n1 += k
		rate = max(k,rate)

	
	n2 = 0 
	for i in xrange(N-1) :
		a, b = m[i], m[i+1]
		n2 += min(rate, a)

	return n1, n2
		

if __name__=='__main__':
	fn = sys.argv[1]
	fp = open(fn)

	T = int(fp.readline().strip())

	for i in xrange(1,T+1) :
		N = int(fp.readline().strip())
		m = [ int(k) for k in fp.readline().split() ]
			
		print "Case #%d:"%i, " %d %d" % solve(N, m)
