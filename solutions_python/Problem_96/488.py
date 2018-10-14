def alp (lem,nsur,men) :
	cont=0
	k=0
	x=len(lem)
	if men==0 :
		return x
	intervalo=((men*3)-2)
	intervalo2=((men*3)-4)
	if intervalo2<0 :
		intervalo2=1
	for i1 in range (x) :
		if (lem[i1] >= intervalo) :
			cont+=1
		elif ((lem[i1] >= intervalo2) and (k<nsur)) :
			k+=1
			cont+=1
	return cont

arq=open("large.in","r")
arq=arq.read()
arq=arq.split()
t=int(arq.pop(0))
for i1 in range(t) :
	res=0
	nemp=int(arq.pop(0))
	nsur=int(arq.pop(0))
	men=int(arq.pop(0))
	lem=[]
	for i2 in range(nemp) :
		lem.append(int(arq.pop(0)))	
	res=alp(lem,nsur,men)
	sai=open("bl.out","a")
	sai.write("Case #" + str(i1+1) + ": " + str (res) + "\n")
