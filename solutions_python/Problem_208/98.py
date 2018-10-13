numruns=int(input())
for run in range(numruns):
	n,tmp=[int(i) for i in input().split()]
	speed=[0]*n
	endur=[0]*n
	for i in range(n):
		endur[i],speed[i]=[int(i) for i in input().split()]
	dist=[max([int(i) for i in input().split()]) for j in range(n)]
	mintime=[10**20]*n
	mintime[0]=0
	for i in range(n):
		d=0
		for j in range(i,n-1):
			d+=dist[j]
			if d<=endur[i]:
				mintime[j+1]=min(mintime[j+1],mintime[i]+d/speed[i])
			else:
				break
	input()
	print('Case #'+str(run+1)+': '+str(mintime[n-1]))