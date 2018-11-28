T = int(raw_input())

def mk(p,f):
	c = 0
	p = fs
	for v in f:
		try: p = p[v]
		except: 
			p[v] = {}
			p = p[v]
			c = c+1
	return c

for CASE in xrange(1,T+1):
	(N,M) = map(int, raw_input().split(' '))

	fs = {}
	for k in xrange(N):
		f = raw_input()[1:].split('/')
		mk(fs,f)
	c = 0
	for k in xrange(M):
		f = raw_input()[1:].split('/')
		c += mk(fs,f)
	print 'Case #'+str(CASE)+': '+str(c)



