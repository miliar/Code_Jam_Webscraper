numruns=int(input())
for run in range(numruns):
	d,n = [int(i) for i in input().split()]
	maxt = -1
	for i in range(n):
		st,sp = [int(i) for i in input().split()]
		maxt = max(maxt,(d-st)/sp)
	print('Case #'+str(run+1)+': '+str(d/maxt))