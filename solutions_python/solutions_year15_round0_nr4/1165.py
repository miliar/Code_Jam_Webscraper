f1=open("me.in","r")
f2=open("me.out","w")
X,M,R,C={},{},{},{}
a=list(map(lambda x:x.split(),f1.readlines()[1:]))
for i in range(1,len(a)+1):
	[X[i],R[i],C[i]]=list(map(lambda x:int(x),a[i-1]))
	if (R[i]*C[i]) % X[i] !=0:
		M[i]='Richard'
	elif X[i]==4 and (R[i],C[i]) in {(4,1),(4,2),(2,2),(2,4),(1,4)}:
		M[i]='Richard'
	elif X[i]==3 and (R[i],C[i]) in {(3,1),(1,3)}:
		M[i]='Richard'
	else:
		M[i]='Gabriel'
m=''
for i in range(1,len(a)+1):
	m=m+'Case'+' '+'#'+str(i)+':'+' '+str(M[i])+'\n'
f2.write(m)
f1.close()
f2.close()

