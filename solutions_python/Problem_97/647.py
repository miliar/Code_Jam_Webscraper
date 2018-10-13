r = [set()]
r+= [{i/10**j+(i%10**j)*10**(k+1-j) for j in xrange(k+2) if i/10**j+(i%10**j)*10**(k+1-j)>i} for k in xrange(6) for i in xrange(10**k,10**(k+1))]
r+= [{i/10**j+(i%10**j)*10**(7-j) for j in xrange(8) if i/10**j+(i%10**j)*10**(7-j)>i} for i in xrange(10**6,2*10**6)]
for T in xrange(input()):
	A,B = map(int,raw_input().split())
	print 'Case #%d: %d'%(T+1,sum(sum(1 for m in r[n] if m<=B) for n in xrange(A,B)))
