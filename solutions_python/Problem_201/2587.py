T=int(input())
for I in range(T):
	temp=input().split()
	N=int(temp[0])
	K=int(temp[1])
	
	room=[False for i in range(N+1)]
	room[N]=True
	for i in range(K):
		Last=-1
		Min=0
		Max=0
		ans=-1
		
		for j in range(N):
			Ls=j-Last-1
			if room[j]:
				Last=j
				continue
			Rs=room[j+1:].index(True)
			if min(Ls,Rs)>Min:
				Min=min(Ls,Rs)
				Max=max(Ls,Rs)
				ans=j
			elif min(Ls,Rs)==Min:
				if max(Ls,Rs)>Max:
					Max=max(Ls,Rs)
					ans=j
		room[ans]=True
		#print(room)
		
		if i==K-1:
			print("Case #"+str(I+1)+": "+str(Max)+" "+str(Min))
		