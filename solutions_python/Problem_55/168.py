f = open('1.in','r')
o = open('out.dat','w')

n = int(f.readline())

for i in xrange(n):
	R,k,N = f.readline().split()
	R = int(R)
	k = int(k)
	N = int(N)
	g = f.readline().split()
	
	g = [int(g[j]) for j in xrange(N)]
	
	y = 0
	
	p  = 0
	for j in xrange(R):
		m = 0
		p0 = p 
		while (m+g[p]) <= k:
			y += g[p]
			m+=g[p]
			
			if (p+1)<N:
				p +=1
			
			else:
				p=0
			
			if p == p0:
				break
			
	
	o.write('Case #' + str(i+1) + ': '+ str(y) +'\n')
	
