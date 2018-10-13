#!/usr/bin/python
from fractions import gcd
TT=input()
for T in range(1,TT+1):
	res="Case #"+str(T)+": "
	ll=raw_input().split();
	n=int(ll[0])
	ans=0
	m=int(ll[1])
	for i in range(2,n+1):
		x=int(ll[i])-int(ll[i-1])
		ans=abs(gcd(ans,x))
		m=min(int(ll[i]),m)
	
	m=m%ans
	if m==0:
		m=ans
	ans=ans-m
	res=res+str(ans)
	print res

