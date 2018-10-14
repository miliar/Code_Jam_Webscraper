for t in range(int(input())):
	n=[int(i) for i in input()[::-1]]
	length=len(n)
	for i in range(1,length):
		if n[i]>n[i-1]:
			n[i]=n[i]-1
			for x in range(i):
				n[x]=9
	print("Case #"+str(t+1)+": ",end="")
	f=0
	for i in range(length-1,-1,-1):
		if n[i]==0:
			f+=1
		else:
			break
	for i in range(length-1-f,-1,-1):
		print(n[i],end="")
	print("")
	