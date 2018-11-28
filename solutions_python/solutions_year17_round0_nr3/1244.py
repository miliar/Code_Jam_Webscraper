from heapq import heappush, heappop
t=int(input())
def urinal(n):
	buff=n//2
	if n%2==0:
		return buff-1,buff
	else:
		return buff,buff
for i in range(t):
	N,k=map(int,input().split())
	cola=[-N]
	for j in range(k):
		n=-heappop(cola)
		L,R=urinal(n)
		heappush(cola,-L)
		heappush(cola,-R)
	print("Case #{}: {} {}".format(i+1, max(L,R),min(L,R)))