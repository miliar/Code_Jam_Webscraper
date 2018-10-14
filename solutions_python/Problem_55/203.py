#!/usr/bin/python
def work():
	ll=raw_input().split()
	r=int(ll[0])
	k=int(ll[1])
	n=int(ll[2])
	ll=raw_input().split()
	#print ll
	a=[]
	for i in range(0,n):
		a.append(int(ll[i]))
	v=[]
	e=[]
	for i in range(0,n):
		s=0
		j=i
		while s+a[j]<=k:
			s+=a[j]
			j+=1
			if j==n:
				j=0
			if j==i:
				break
		e.append(j)
		v.append(s)
	ans=0
	j=0
	for i in range(0,r):
		ans+=v[j]
		j=e[j]
	return ans

TT=input()
for T in range(1,TT+1):
	ans=work()
	res="Case #"+str(T)+": "+str(ans)
	print res
