t=int(input())
i=1
while(t):
	n=int(input())
	if(n>=1 and n<=9):
		s = "Case #"+str(i)+":"
		print(s,n)
	else:
		while(n>=11):
			f=0
			n=str(n)
			for x in range(len(n)-1):
				if(ord(n[x])>ord(n[x+1])):
					f=1
					break
			if(f==0):
				s = "Case #"+str(i)+":"
				print(s,n)
				break
			else:
				n=int(n)
				n=n-1
	i=i+1
	t=t-1


				



