import math

T = int(raw_input().strip())
for t in xrange(1,T+1):
	s,ks = raw_input().strip().split()
	k = int(ks)
	n = len(s)
	#print s, k
	ans = 0
	flip = [0]*n*2
	nf = 0
	ok = True
	for i in xrange(0,n):
		nf += flip[i]
		if s[i] == '+':
			c = 0
		else:
			c = 1
		c = (c+nf)%2
		if c == 1:
			ans += 1
			flip[i+k] += 1
			nf += 1
			if n-k < i:
				ok = False
	
	if not ok:
		print "Case #%d: IMPOSSIBLE"%(t)
	else:
		print "Case #%d: %d"%(t,ans)

