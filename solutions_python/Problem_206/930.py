from math import *

T=int(raw_input())
for t in range(1,T+1):
	D,N=map(int,raw_input().split())
	horses=[]
	for i in range(N):
		horses.append(map(int,raw_input().split()))

	maxTime=0
	for horse in horses:
		maxTime=max(maxTime,(D-horse[0])*1.0/horse[1])
	res=D*1.0/maxTime

	print("Case #%d: %s" % (t,str(res)))


