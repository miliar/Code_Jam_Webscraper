inFile = open("C-large.in")
outFile = open("result.out", "w")
x=[]
for line in inFile:
	x.append(line)
t =int(x[0])

for i in range(t):
	a=[[],[]]
	n,k=map(int,x[i+1].strip().split(" "))
	a[0].append(n/2)
	a[1].append(1)
	max=n/2
	if(n%2==0):
		a[0].append(n/2-1)
		a[1].append(1)
		min=n/2-1
	else:
		a[1][0]+=1
		min=n/2
	k-=1
	while k>0:
		if a[0][0]/2 not in a[0]:
			a[0].append(a[0][0]/2)
			a[1].append(a[1][0])
		else:
			a[1][a[0].index(a[0][0]/2)]+=a[1][0]
		max=a[0][0]/2
		if(a[0][0]%2==0):
			if a[0][0]/2-1 not in a[0]:
				a[0].append(a[0][0]/2-1)
				a[1].append(a[1][0])
			else:
				a[1][a[0].index(a[0][0]/2-1)]+=a[1][0]
			min=a[0][0]/2-1
		else:
			a[1][a[0].index(a[0][0]/2)]+=a[1][0]
			min=a[0][0]/2
		if k<a[1][0]:
			break
		k-=a[1][0]
		a[0].pop(0)
		a[1].pop(0)
	outFile.write("Case #"+str(i+1)+": "+str(max)+" "+str(min)+"\n")
	
	#outFile.write("Case #"+str(i+1)+": "+str(int("".join(n)))+"\n")
	
inFile.close()
outFile.close()
