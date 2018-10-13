#!/usr/bin/pypy
import sys
if sys.version_info[0]<=2:
	range=xrange
	input=raw_input

def solve2(n,k):
	l,r=n//2,(n-1)//2
	arr=[[l,r,1]]
	while k:
		l,r,cnt=arr[0]
		if cnt>=k:
			break
		del arr[0]
		k-=cnt
		lr=[l//2,(l-1)//2,cnt]
		if arr and arr[-1][0]==lr[0] and arr[-1][1]==lr[1]:
			arr[-1][2]+=cnt
		else:
			arr.append(lr)
		lr=[r//2,(r-1)//2,cnt]
		if arr and arr[-1][0]==lr[0] and arr[-1][1]==lr[1]:
			arr[-1][2]+=cnt
		else:
			arr.append(lr)
	return " ".join(map(str,arr[0][:2]))

cases=int(input().strip())
for cs in range(1,cases+1):
	n,k=map(int,input().strip().split())
	print("Case #"+str(cs)+": "+str(solve2(n,k)))
