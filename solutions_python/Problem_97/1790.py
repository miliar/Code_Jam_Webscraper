def valido(a,b):
	if int(b)<=B and b[0]!="0" and a!=b:
		return True
	else:
		return False



T=int(raw_input(""))

for X in range(T):
	entrada=str(raw_input("")).split(" ")
	A=int(entrada[0])
	B=int(entrada[1])
	c=0
	lista=[]
	lista2=[]
	lista3=[]
	lista4=[]
	for i in range(1+(B-A)):
		n=str(A+i)
		lista.append(n)

		for j in range(len(n)-1):
			m=n[len(n)-(j+1):]+n[:len(n)-j-1]
			if valido(n,m) and lista.count(m)==0 and lista2.count(m+n)==0:
				c+=1
				lista3.append(n)
				lista4.append(m)
#				print j+1,n,m,"ok"
			lista2.append(m+n)
	desc=0
	for k in lista4:
		if lista.count(k)!=0:
			desc+=1
	print "Case #"+str(X+1)+": "+str(desc)

