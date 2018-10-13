for t in range(int(input())):
	l=[int(i) for i in input()]
	i = len(l)-1
	j = i + 1
	while i>0:
		if l[i]<l[i-1] :
			while l[i-1]==0:
				i-=1
			if i == 1 and l[i-1] == 1:
				d=[9 for k in range(len(l)-1)]
				l=d
			else:
				for m in range(i,j):l[m] = 9
				j = i+1		
				l[i-1] -= 1
		i-=1			
	ans =""
	for i in l:ans+=str(i)
	print("case #"+str(t+1)+":",ans)	
	
