'''
Cookie Clicker Alpha
'''
if __name__ == '__main__':
	f=open("B-large.in")
	nc=int(f.readline())
	for x in xrange(1,nc+1):
		r = 2.0
		(C, F, X) = map(float, f.readline().strip('\n').split(' '))
		# Alg
		s0 = X / r
		a = 0
		k=0
		s = 999999999
		while s0 < s:
			s = s0
			a += C / r
			s0 = a + X / (r + F)
			k += 1
			r += F
			
		print "Case #%d: %.7f" % (x, s)
		
			
