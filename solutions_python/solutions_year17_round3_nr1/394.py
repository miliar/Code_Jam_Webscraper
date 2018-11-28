from math import *
from sys import *

setrecursionlimit(1000000)

T=int(raw_input())
for t in range(1,T+1):
	N,K=map(int,raw_input().split())
	pans=[] #(R,H)
	for i in range(N):
		pans.append(map(int,raw_input().split()))
	pans.sort(reverse=True)
	memo=[[-1]*1001 for i in range(1001)]

	def getMax(index,rem):
		if index==N or rem==0:
			return 0

		if memo[index][rem]!=-1:
			return memo[index][rem]

		#select
		select=2*pi*pans[index][0]*pans[index][1]
		if rem==K:
			select+=pi*(pans[index][0]**2)
		select=select+getMax(index+1, rem-1)

		#not select
		notSelect=getMax(index+1, rem)

		memo[index][rem]=max(select,notSelect)
		return memo[index][rem]

	res=getMax(0,K)

	print("Case #%d: %s" % (t,str(res)))
