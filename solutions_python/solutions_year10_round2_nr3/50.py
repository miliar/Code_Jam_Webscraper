from math import *
inf = open("file.in")
ouf = open("file.out","w")
counttests = int(inf.readline().split()[0])
case = 0
def answer(x):
	global case, counttests
	if case > counttests:
		exit
	case += 1
	print >>ouf, "Case #"+str(case)+": "+str(x)
	print "Case #"+str(case)+": "+str(x)

def fact(x): return (1 if x==0 else x * fact(x-1))

def cnk(n,k):
	if n<k or k<0 or n<0:
		return 0
	else:
		return fact(n)/fact(k)/fact(n-k)%100003

def rec(n,k):
	global dyn
	if n<=k:
		return 0
	if dyn[n][k]==0:
		for i in xrange(n):
			dyn[n][k]+=rec(k,i)*cnk(n-k-1,k-i-1)
			dyn[n][k]%=100003
	return dyn[n][k]

dyn = []
for i in xrange(1000):
	dyn.append([0]*(1000))
for i in xrange(1000):
	dyn[i][0] = 0
	dyn[i][1] = 1

print rec(3,2)
for iii in xrange(counttests):
	n = int(inf.readline().split()[0])

	res=0
	for i in xrange(n):
		res = (res+rec(n,i))%100003
	answer(res)
