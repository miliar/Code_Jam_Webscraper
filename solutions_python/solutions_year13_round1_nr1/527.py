from math import sqrt

from decimal import *
getcontext().prec = 100
f= open("input.txt")
c=int(f.readline())
def d2(r,t):
	r=Decimal(r)
	t=Decimal(t)
	return (Decimal(Decimal(4)*r**Decimal(2)-Decimal(4)*r+Decimal(8)*t+Decimal(1)).sqrt()-Decimal(2)*r-Decimal(3))/Decimal(4)
for l in range(c):
	v=f.readline().split()
	r=int(v[0])
	t=int(v[1])
	top = d2(r,t)+1
	print ("Case #"+str(l+1)+": "+str(int(top)))










