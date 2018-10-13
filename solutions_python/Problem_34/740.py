inp=open("alien.in","r");

t=inp.readlines()

z=t[0].split(' ')
print z
L=int(z[0]);
D=int(z[1]);
N=int(z[2]);

wordlib=t[1:D+1]

for ind in xrange(D+1,len(t)):
	wd=t[ind]
	cpos=[i for i in wordlib]
	hopar=False
	ccharpos=0;
	nposs=[]
	for i in xrange(0,len(wd)-1):
		cha=wd[i]
	#	print 'curr char:',cha
		if cha=='(':
			hopar=True
		elif cha==')':
			hopar=False
			ccharpos+=1
		else:
			for pwd in cpos:
	#			print "\t testing against",pwd,pwd[ccharpos]
				if pwd[ccharpos]==cha:
					nposs.append(pwd)
	#				print '\t\tyay'
			if not hopar:
				ccharpos+=1
		if not hopar:
			cpos=[i for i in nposs]
			nposs=[]
	print "Case #%i: %i"%(ind-D,len(cpos))

			
