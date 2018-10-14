import sys
f = sys.stdin

import fractions


t = int(f.next())
for c in xrange(1, t+1):
    n, pd, pg = map(int, f.next().split())
    gcd = fractions.gcd(pd, 100)
    if pg == 100 and pd < 100:
        flag = False
    elif pg == 0 and pd > 0:
        flag = False
    elif 100/gcd > n:
        flag = False
    else:
        flag = True
    
    if flag:
        print "Case #%d: Possible" % c
    else:
        print "Case #%d: Broken" % c
        
