f=open('A-small-attempt1.in','r')
p=open('o','w+')
t=int(f.readline())
ti=1
while ti<=t:
	a1=int(f.readline())
	ai=0
	while ai<a1-1:
		f.readline()
		ai+=1
	l1=f.readline().split()
	ai+=1
	while ai<4:
		f.readline()
		ai+=1
	a2=int(f.readline())
	ai=0
	while ai<a2-1:
		f.readline()
		ai+=1
	l2=f.readline().split()
	ai+=1
	while ai<4:
		f.readline()
		ai+=1
	
	l=[v for v in l1 if v in l2]
	if len(l)==0:
		s= str("Case #")+str(ti)+str(": Volunteer cheated! \n")
	elif len(l)>1:
		s= str("Case #")+str(ti)+str(": Bad magician! \n")
	else:
		s= str("Case #")+str(ti)+str(": ")+str(l[0])+str(" \n")
	p.write(s)
	ti+=1