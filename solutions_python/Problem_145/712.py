
from fractions import gcd
import math
def rec(p,q):
	t=float(float(p)/q)
	if t>=0.5:
		return 1
	else:
		return 1+rec(p*2,q)
t=int(raw_input())
for ca in range(1,t+1):
	aa=raw_input()
	a=aa.split("/")
	p1,q1=a
	p=float(p1)
	q=float(q1)
	t=float(float(p)/q)
	c =math.log(q,2)
	d=int(c)
	if(d!=c):
		ans="impossible"
	else:
		ans=str(rec(p,q))
		



	print "Case #%i: %s" %(ca,ans)
