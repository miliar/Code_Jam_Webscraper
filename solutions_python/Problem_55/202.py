sun=input()
pra=1
while pra<=sun:
	print "Case #"+str(pra)+":",
	l=raw_input()
	ll=l.split(' ')
	R=int(ll[0])
	K=int(ll[1])
	N=int(ll[2])

	l=raw_input()
	ll=l.split(' ')

	arr=[]
	for j in ll:
		arr.append(int(j))

	ans=0
	j=0
	kk=0
	while j<R:
		temp=0
		round=kk%N
		while(K-temp>0 and arr[kk%N]<=K-temp):
			temp+=arr[kk%N]
			kk+=1
			if round==kk%N:
				break
		j+=1
		ans+=temp
	print ans
	pra+=1
