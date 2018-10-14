def ch(n):
	nn=str(n)
	n1=list(nn)

	i=len(nn)
	i=i-1
	ik=i-1
	while i>0:
		if(nn[ik]>nn[i]):
			return False
		else:
			ik=ik-1
			i=i-1
	return True


file = open('a.txt', 'r') 
k=file.readline()
jj=int(k)

ii=1

print jj
file1= open('b.txt','w')

while ii<=jj:
	k=file.readline()
	k1=int(k)
	print k1
	while k1>0:
		if(ch(k1)):
			file1.write('Case #'+str(ii)+': '+str(k1)+'\n')
			break;
		else: 
			k1=k1-1
	ii=ii+1
file.close()
file1.close()
