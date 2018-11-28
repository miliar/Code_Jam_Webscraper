#Problem: Snapper
#http://code.google.com/codejam/contest/dashboard?c=433101#

import sys

def binary2(n):
    if n == 0:
        return ['0']
    buf=[]
    d=n
    while d > 0:
        buf.append(d%2)
        d /= 2
    return buf

def snapper(n,k):
    if k == 0:
        return 'OFF'
    d = binary2(k)
    if d[:n] == [1]*n:
        return 'ON'
    return 'OFF'
    
tests = int(sys.stdin.readline())
for test in range(0, tests):
    (z1, z2) = sys.stdin.readline().split(' ')
    n=int(z1)
    k=int(z2)
    print "Case #%d: %s" % (test+1, snapper(n, k))


##print snapper(1, 0)

##	
##print snapper(1,0)
##print snapper(1,1)
##print snapper(4,0)
##print snapper(4,47)

