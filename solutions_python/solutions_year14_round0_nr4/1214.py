f=open('D-large.in','r')
p=open('od','w+')
t=int(f.readline())
ti=1;
while ti<=t:
	# print ti
	nb=int(f.readline())
	na=[float(v) for v in f.readline().split()]
	kn=sorted([float(v) for v in f.readline().split()],reverse=True)
	rna=na[:]
	rkn=kn[::-1]
	rw=0
	while len(rkn)>0:
		cn=rna.pop(0)
		s=0
		for ck in rkn:
			if ck > cn:
				rkn.pop(rkn.index(ck))
				s=1
				break
		if s==0:
			rw+=1
			rkn.pop(0)

	# rw=nb-rw
	na=sorted(na)
	dw=0
	while len(na)>0:

		while len(na)>0 and na[len(na)-1]>kn[0]:
			na.pop()
			kn.pop(0)
			dw+=1
		if len(na)==0:
			break
		cn=na.pop(0)
		if cn < kn[0]:
			kn.pop(0)	

		while len(na)>0 and na[len(na)-1]>kn[0]:
			na.pop()
			kn.pop(0)
			dw+=1

		# print dw,'\t',rw
	s= str("Case #")+str(ti)+str(": ")+str(dw)+str(' ')+str(rw)+str(" \n")
	p.write(s)
	ti+=1