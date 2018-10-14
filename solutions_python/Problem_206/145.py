# Google Codejam 2017: Round 1B
# Problem A: Steed 2: Cruise Control
# Author: Mahmoud Aladdin <aladdin3>

import sys

def solve(cn):
    d, n = map(int, raw_input().strip().split())
    
    mxTime = -1
    for i in xrange(n):
        ki, si = map(int, raw_input().strip().split())
        diff = (d - ki + 0.0)
        time = diff / si
        mxTime = max(time, mxTime)
    
    speed = d / mxTime
    print "Case #{0}: {1:0.8f}".format(cn, speed)
    print >> sys.stderr, "Case #{0}: {1:0.8f}".format(cn, speed)
    

if __name__ == "__main__":
    cn = input()
    for i in xrange(cn):
        solve(i + 1)