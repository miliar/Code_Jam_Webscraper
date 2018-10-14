from math import sqrt
T = int(raw_input())

for k in range(1,T+1):
    print "Case #"+str(k)+":",
    r,t = [int(x) for x in raw_input().split()]
    print int(( 1 - 2*r + sqrt( (2*r -1)**2 + 8 * t))/4)
