inFile = open("B-small-attempt3.in")
outFile = open("result.out", "w")
x=[]
for line in inFile:
	x.append(line)
t =int(x[0])
for i in range(t):
	n=x[i+1].strip()
	print  n
	#c=n[0]
	c1=1
	j=0
	while j<len(n)-1:
		if n[j]>n[j+1]:
			break
		if n[j]==n[j+1]:
			c1+=1
		else:
			#c=n[j+1]
			c1=1
		j+=1
	print j,c1
	if len(n)==1 or j==len(n)-1:
		outFile.write("Case #"+str(i+1)+": "+str(n)+"\n")
	else:
		#print c1
		l=len(n)
		#print l
		n=list(n)
		#print n
		if c1>1:
			n[l-c1-1]=chr(ord(n[l-c1-1])-1)
		else:
			n[j]=chr(ord(n[j])-1)
			c1=l-j-1
		for k in range(l-c1,l):
			n[k]='9'
		#print n
		outFile.write("Case #"+str(i+1)+": "+str(int("".join(n)))+"\n")
		print n
inFile.close()
outFile.close()
