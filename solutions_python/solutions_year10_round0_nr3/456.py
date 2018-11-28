#Problem: Theme Park
#http://code.google.com/codejam/contest/dashboard?c=433101#s=p2

import sys

def roller(r, k, g):
    res = 0
    buf = g[:]
    if len(g)<1 or k < 1:
        return 0
    for i in range(r):
        cap = 0
        size=len(g)
        while 1:
            top = buf[0]
            if  top+cap > k:
                break
            if size < 1:
                break
            
            cap += top
            buf.append(top)
            buf.pop(0)
            size -= 1
        res += cap
    return res

tests = int(sys.stdin.readline())
for test in range(0, tests):
    (z1, z2, z3) = sys.stdin.readline().split(' ')
    r=int(z1)
    k=int(z2)
    n=int(z3)
    groups = sys.stdin.readline().split(' ')
    for x in range(n):
        groups[x] = int(groups[x])
    print "Case #%d: %s" % (test+1, roller(r, k, groups))


##print roller(4, 6, [1, 4, 2, 1])
###should be 21
##
##print roller(100,  10, [1])
###should be 100
##
##print roller(5, 5, [2, 4, 2, 3, 4, 2, 1, 2, 1, 3])
###should be 100
##
##print roller(100, 0, [])
###should be 


