#p='B-small-attempt0.in'
p='B-large.in'
in1 = open(p,'r')
T = in1.readline()
for t in range(int(T)):
	C,F,X=map(float,in1.readline().strip().split())
	
	inc=2
	xx=0
	tt=0
	
	while xx+C<X:
		tc=C/inc
		tt+=tc
		xx+=C
		if ((X-xx)/inc) <((X-xx+C)/(inc+F)):
			tt+=(X-xx)/inc
			xx=X
		else:
			xx-=C
			inc=inc+F
	
	if tt==0:
		tt=X/2
	r='%.7f'%(tt)
	print 'Case #{}: {}'.format(t+1,r)