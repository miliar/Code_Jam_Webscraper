f = open('1.in','r')
o = open('out.dat','w')

t = int(f.readline())

for i in xrange(t):
	o.write('Case #' + str(i+1) + ': ')
	
	n = int(f.readline())
	
	A = []
	
	for j in xrange(n):
		A.append([int(x) for x in f.readline().split()])
	
	c = 0
	
	for j in xrange(n-1):
		for k in xrange(j,n):
			
			if A[j][0] > A[k][0] and A[j][1] < A[k][1]:
				c += 1
				
			elif A[j][0] < A[k][0] and A[j][1] > A[k][1]:
				c += 1
				
	o.write(str(c))
	o.write('\n')