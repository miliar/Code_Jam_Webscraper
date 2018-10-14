f=open(r'cheb_B_smallinput.in', 'r')
n=f.readline()
n=n.rsplit( )[0]
n=int(n)
# print n
for i in range(1, n+1) :
	line=f.readline()
	line=line.rstrip("\n\r ")	
	line=line.split(' ')
	C=float(line.pop(0))
	F=float(line.pop(0))
	X=float(line.pop(0))
	cont = 1
	nF=0
	cT=0
	T=X/2
	t=T
	while(cont) :
		if(nF != 0) : cps1=2+(nF-1)*F
		cps=2+nF*F
		# print 'cps = {0}'.format(cps)
		if(nF != 0) :
			cT = cT+C/cps1
			t=cT+X/cps
		if(t<=T) :
			T=t
			nF=nF+1
			# print 'cT = {0}'.format(cT)
			# print 'T = {0}'.format(T)
			# print 'nF = {0}'.format(nF)
		else :
			cont=0
	# print 'C = {0}, F = {1}, X = {2}'.format(C, F, X)
	print 'Case #{0}: {1}'.format(i, T)
