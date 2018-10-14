dirt=[]
k=1
t=input()
for j in range(t):
	n=input();w=n
	while(w):
		c=0;ar=[];t=0;h=0
		n=w;q=(n)%10;m=0
		while(n):
			d=n%10
			if c>=1:
				if q<d:
					break
			ar.append(d);ar.append(q)
			q=d;n/=10;
			if t!=0:
				if ar[t]!=ar[t-1]:m+=1
					
			c+=1;t+=1
		if n==0:
			dirt.append(w)
			break
		w=w-10**m
for i in dirt:
	print "Case #{0}: {1}".format(k,i)
	k+=1
