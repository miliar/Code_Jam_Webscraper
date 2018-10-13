dirt=[]
k=1
t=input()
for j in range(t):
	n=input();w=n
	while(w):
		c=0;n=w
		while(n):
			d=n%10
			if c!=0:
				if q<d:
					break
			q=d;c=1;n/=10
		if n==0:
			dirt.append(w)
			break
		w-=1
for i in dirt:
	print "Case #{0}: {1}".format(k,i)
	k+=1
