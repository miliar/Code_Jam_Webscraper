f = open('input.txt')
t = int(f.readline().rstrip('\n'))

for case in range (1,t+1):
	nStr=f.readline().rstrip('\n')
	n=int(nStr)
	k=len(nStr)
	for i in range(0,len(nStr)-1):
		if(int(nStr[i])>int(nStr[i+1])):
			k=i
			break

	if(k==len(nStr)):
		print("Case #"+str(case)+": "+nStr)
	else:
		while(k>0 and nStr[k]==nStr[k-1]) :k=k-1


		tidy = nStr[:k]+str(int(nStr[k])-1)
		for i in range (0,len(nStr)-k-1):
			tidy = tidy+"9"

		l = 0
		while(l<len(tidy) and tidy[l]=="0") : l=l+1


		print("Case #"+str(case)+": "+tidy[l:])


