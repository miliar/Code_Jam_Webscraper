def sel(i,n,a):
	global ans
	ans=min(ans,i+max(a))
	if (i!=n):
		m=max(a)
		for x in range(1,(m+1)/2+1):
			b=list(a)
			b.remove(m)
			b.append(x)
			b.append(m-x)
			sel(i+1,n,b)


t=input()
tt=1
while tt<=t:
	n=input()
	a=map(int,raw_input().split())
	ans=max(a)
	sel(0,ans,a)		
	print "Case #"+str(tt)+": "+str(ans)
	tt+=1