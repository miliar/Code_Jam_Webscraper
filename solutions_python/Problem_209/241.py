from math import pi
from heapq import *

for xyz in range(1,int(input())+1):
	print("Case #"+str(xyz)+': ',end='')
	n,k = map(int,input().split())
	a = []
	for _ in range(n):
		a.append(list(map(int,input().split())))
	a.sort(reverse = True)
	ans = 0
	cnt = 0
	h = []
	cur = 0
	pref = 0
	# print(a)
	for i in range(n-1,-1,-1):
		cnt += 1
		pref += a[i][0]*a[i][1]
		if cnt > k:
			x = heappop(h)
			pref -= x
		heappush(h,a[i][0]*a[i][1])	
		if cnt >= k:	
			ans = max(ans,(pi*(a[i][0]**2))+(2*pi*pref))
	print(ans)				

