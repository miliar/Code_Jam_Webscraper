T=input()
for t in xrange(T):
	b,n = map(int,raw_input().split())
	m = map(int,raw_input().split())
	lim=10
	for i in xrange(lim):
		m = m+m
	def foo(f):
		a=1
		a1=10**30
		while a<=a1:
			b1=(a+a1)/2
			temp1=0
			for i in xrange(f):
				temp1 = temp1+ (b1+m[i]-1)/m[i]
			for i in xrange(f,b):
				temp1 = temp1+ (b1-1+m[i]-1)/m[i]
			if (temp1<n) :
				a = b1+1
			else:
				a1 = b1-1
		return a1+1
	out=[10**15,b+1]
	for ans in xrange(1,b+1):
		x = foo(ans)
		if out[0] > x :
			out[0] = x
			out[1] = ans
	
	print 'Case #%d: %d' % (t+1,out[1])