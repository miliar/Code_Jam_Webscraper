def tr(s):
	a=int(s.split()[0])
	b=int(s.split()[1])
	res=0
	spp=[]
	
	for i in range(a,b+1):
		si=str(i)
		if len(si)==1:
			continue
		if spp:
			if (i in [x[0] for x in spp]) or (i in [x[1] for x  in spp]):
				continue
		tt=0
		sp3=[]
		for k in range(len(si)):
			
			si1=si[1:]+si[0]
			if [int(si1),int(si)] in spp or [int(si),int(si1)] in spp:
				si=si1
				continue
	 		p1=int(si)
			if p1==int(si1):
				si=si1
				continue
				
			p=int(si1)
			if p>=a and p<=b:
				
				tt+=1
				spp.append([p,p1])
				if not p in sp3:
					sp3.append(p)
				if p1>=a and p1<=b:
					if not p1 in sp3:
						sp3.append(p1)
				
			si=si1
		tt=len(sp3)
		res+=tt*(tt-1)/2
		
				
	return res

	

file = open('c.in','r')

t=int(file.readline())
ret=[]
for x in file.readlines():
	x=x.replace('\n','')
	x=x.replace('\r','')
	ret.append(tr(x))
file2=open('c.out','w')
for x in range(len(ret)):
	file2.write('Case #'+str(x+1)+': '+str(ret[x])+'\n')
file2.close()
file.close()

