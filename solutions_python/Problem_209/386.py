import numpy as np
import math

t = int(raw_input())

for z in range(1,t+1):

    n,k = map(int, raw_input().split(' '))

    a = []
    u = []

    l = 0.0

    for _ in range(n):
        x,y = map(int, raw_input().split(' '))
        u.append((x,y))

    for i in range(n):
	    
	    p = u[i]
	    a = list(u)
	    a.pop(i)
	    b = []

	    for x in a:
	    	b.append(x[0]*x[1])

	    ans = 0

	    b.sort()
	    o = len(b)   

	    for i in range(k-1):
	    	ans += b[o-i-1]*2*math.pi

	    ans += math.pi*p[0]*p[0] + 2*math.pi*p[0]*p[1]

	    l = max(l,ans)

    print "Case #%d: %.10f" %(z,l)

