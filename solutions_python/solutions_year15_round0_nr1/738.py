T=int(raw_input().strip())
for t in range(T):
	N,shynes=raw_input().strip().split()
	N=int(N)
	res=0
	curr=int(shynes[0])
	for i in range(1,N+1):
		to_invite=max(0,i-curr)
		res+=to_invite
		sh=int(shynes[i])
		curr+=sh+to_invite
	print "Case #"+str(t+1)+": "+str(res)