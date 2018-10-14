filename="A-large"
infile=open(filename+".in")
outfile=open(filename+".out","w")
for i in range(int(infile.readline())):
	line=infile.readline()
	Smax=int(line[:line.index(' ')])
	Slist=line[(line.index(' ')+1):]
	friends=0
	stov=0
	k=0
	print Slist.strip()
	for j in Slist.strip():
		print (k,stov,friends,j)
		if k>stov:
			friends+=k-stov
			stov+=int(j)+(k-stov)
		else:
			stov+=int(j)
		k+=1

	outfile.write('Case #'+str(i+1)+': '+str(friends)+'\n')