def rec(st1,st2) :
	l1=len(st1)
	i2=int(st2)
	for i in range (l1) :
		aux=st1[i:]+st1[:i]
		i1=int(aux)
		i2=int(st2)
		if i1==i2 :
			raw_input()
			return True
	return False

def verrec (a,b) :
	p=0
	for i1 in range (a+1,b+1) :
		aux1=str(i1)
		l1=len(aux1)
		laux=[]
		for i2 in range (l1) :
			aux=aux1[i2:]+aux1[:i2]
			if aux[0] != '0' :	
				aux=int(aux)
				if aux not in laux :
					if aux >= a and aux < i1 :
						p+=1
					laux.append(aux)
	return p

arq=open("large.in","r")
arq=arq.read()
arq=arq.split()
t=int(arq.pop(0))
##t=int(raw_input("Testes : "))
for c1 in range (t) :
	a=int(arq.pop(0))
	b=int(arq.pop(0))
##	a=int(raw_input("A : "))
##	b=int(raw_input("B : "))
	p=verrec(a,b)
	sai=open("large.out","a")
##	print p
	sai.write("Case #" + str(c1+1) + ": " + str(p) + "\n")
