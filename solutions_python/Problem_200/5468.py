dirt=[]
k=1
t=input()
for j in range(t):
	n=input();w=n
	while(w):
		c=0;g=n%10
		n=w;q=(n)%10;m=-2
		while(n):
			d=n%10
			if c>=1:
				if q<d:
					break
			q=d;n/=10;
			
			c+=1;g=d
		if n==0:
			dirt.append(w)
			break
		w=w-1
for i in dirt:
	print "Case #{0}: {1}".format(k,i)
	k+=1
