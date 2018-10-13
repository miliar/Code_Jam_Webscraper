
DEBUG=0


def tleft( C,F,X, farms):
	rate=2.0+farms*F
	return (X)/rate

def Solve(C,F,X, farms=0):
	t=0
	while 1:
		if DEBUG: print "Solve(",C,F,X,farms, t
		if X<C:
			return t+tleft(C,F,X, farms)
		
		dt1a=tleft(C,F,C,farms)
		dt1b=tleft(C,F,X,farms+1)
		
		dt2=tleft(C,F,X,farms)
		if DEBUG: print 'dt1a',dt1a,'dt1b',dt1b,'dt2',dt2,'decision',
		if dt1a+dt1b<dt2:
			if DEBUG: print 'farm'
			farms+=1
			t+=dt1a
		else:
			if DEBUG: print 'no farm'
			return dt2+t
		

filename='B-large-0'
f=file('%s.in'%filename, 'r')
of=file('%s.out'%filename, 'w')
T=int(f.readline())
for t in range(T):
	la=f.readline().split(' ')
	la=[float(x) for x in la]
	if DEBUG: print la
	C, F, X=la
	s1=Solve(C,F,X)
	if DEBUG: print 'S:',s1
	of.write( "Case #%d: %f\n"%(t+1, s1))
