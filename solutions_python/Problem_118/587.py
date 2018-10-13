def ok(x):
	a=[]
	while x>0:
		a.append(x%10)
		x/=10
	n=len(a)
	for i in range(n/2):
		if a[i]!=a[n-i-1]:
			return 0
	return 1

global a
def bs(x):
	l=0
	r=len(a)-1
	ret=0
	while l<=r:
		mid=(l+r)//2
		if a[mid]<=x:
			ret=mid
			l=mid+1
		else:
			r=mid-1
	return ret
	
def ts(x):
	l=0
	r=len(a)-1
	ret=0
	while l<=r:
		mid=(l+r)//2
		if a[mid]<x:
			ret=mid
			l=mid+1
		else:
			r=mid-1
	return ret
	
t=int(raw_input())
a=[]
for i in range(10000000):
	if ok(i) and ok(i*i):
		a.append(i*i)
for test in range(t):
	l,r=map(int,raw_input().split())
	print "Case #"+str(test+1)+":",bs(r)-ts(l)