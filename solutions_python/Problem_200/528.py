from math import *

T=int(raw_input())
for t in range(1,T+1):
	N=map(int,list(raw_input()))
	start9=-1
	for i in range(len(N)-2,-1,-1):
		if N[i]>N[i+1]:
			N[i]-=1
			start9=i+1
	if start9!=-1:
		for i in range(start9,len(N)):
			N[i]=9
	print("Case #%d: %d" % (t,int(''.join(map(str,N)))))