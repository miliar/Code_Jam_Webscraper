def isRecycled(n,m):
	if(len(n)==1):
		return(False)
	for i in range(1,len(n)):
		if(int(n[i:]+n[:i])==int(m)):
			#print n,m
			return(True)
	return(False)
f = open("recycled.txt","r")
t = f.readline()
case = 1
for line in f:
	sp = line.split(' ')
	count = 0
	found = []
	a = int(sp[0])
	b = int(sp[1])
	#print a,b
	for i in range(a,b):
		for j in range(i+1,b+1):
			if(len(str(i))!=len(str(j))):
				break
			else:
				if(isRecycled(str(i),str(j))):
					count = count + 1
					#found.append((i,j))
					#break
	print "Case #"+str(case)+": "+str(count)
	case = case + 1
	#print "----------------------------- end --------------------------------"