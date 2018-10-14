def f(a):
	N=len(a)
	M=len(a[0])
	for i in range(0,N):
		for j in range(0,M):
			if min(max([a[i][x] for x in range(0,M)]),max([a[x][j] for x in range(0,N)]))>a[i][j]:return 1
	return 0
T=int(raw_input())
n=""
for k in range(1,T+1):
	N=int(raw_input().split()[0])
	a=[]
	for K in range(1,N+1):
		a.append(map(lambda x:int(x),raw_input().split()))
	if f(a)==1:n+="Case #"+str(k)+": NO"+"\n"
	else:n+="Case #"+str(k)+": YES"+"\n"
print n
