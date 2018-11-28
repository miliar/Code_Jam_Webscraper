def tidy(n):
	k,m,count=(n,0,0)
	l=[]
	while(k>0):
		l.append(int(k%10))
		k=int(k/10)
	for i in range(len(l)):
		if(i!=len(l)-1):
			if (l[i]<l[i+1]):
				(l[i],l[i+1])=(9,l[i+1]-1)
				count=i
				while(count>0):
					l[i-count],count=(9,count-1)
	for j in l[::-1]:
		m=m*10+j			
	return m	
t=int(input())
for i in range(1,t+1):
        m = int(input())
        n=tidy(m)
        print("Case #{}: {}".format(i,n))
