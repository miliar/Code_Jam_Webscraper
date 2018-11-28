def func(N,K):
	if N==K:return 0,0
	n=N-1
	a=n//2
	b,k=n-a,K-1
	p=k//2;q=k-p
	if 1==K:return b,a
	if 1==K:return func(b,1)
	if 0==(n%2):return func(b,q)
	else:
		if 0==(k%2):return func(a,p)
		else:return func(b,q)
			
for i in range(1,input()+1):
	N,K =map(int,raw_input().split())
	r=func(N,K)
	print "Case #"+str(i)+": "+str(r[0])+" "+str(r[1])
