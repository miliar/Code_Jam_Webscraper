from math import inf
t=int(input())
for i in range(t):
	minV=inf
	D,N=map(int,input().split())
	for j in range(N):
		Ki,Si=map(int,input().split())
		minV=min(minV,Si*D/(D-Ki))
	print("Case #{}: {}".format(i+1, minV))