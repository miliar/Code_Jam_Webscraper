from math import *

T=int(raw_input())
for t in range(1,T+1):
	perc,K=raw_input().split()
	perc=list(perc)
	N=len(perc)
	K=int(K)
	res=0
	for i in range(N-(K-1)):
		if perc[i]=='-':
			res+=1
			for j in range(1,K):
				perc[i+j]='+' if perc[i+j]=='-' else '-'
	for i in range(N-1-(K-2),N):
		if perc[i]=='-':
			res=-1

	print("Case #%d: %s" % (t,str(res) if res!=-1 else "IMPOSSIBLE"))