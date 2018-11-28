T=int(input())
t=1
while t<=T:
	N,K=map(int,input().split())
	N=[N]
	while K:
		mx=max(N)
		pos=N.index(mx)
		if mx%2==0:
			N=N[:pos]+[mx//2-1,mx//2]+N[pos+1:]
		else:
			N=N[:pos]+[mx//2,mx//2]+N[pos+1:]
		K=K-1
		# print(''.join(map(str,N)))
	# print("OUTSIDE")
	print("Case #"+str(t)+": "+str(N[pos+1])+" "+str(N[pos]))
	t=t+1