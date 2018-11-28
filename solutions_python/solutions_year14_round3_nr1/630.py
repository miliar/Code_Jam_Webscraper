#/usr/local/bin/python

import sys
import math

T = int(sys.stdin.readline())

for caseno in xrange(T):
    P, Q = [int(x) for x in sys.stdin.readline().split('/')]
    ans =  1

    ans = 0

    while (Q % 2) == 0:
        Q /= 2
        ans += 1

    #print ans, Q

    if P % Q == 0:
       P /= Q
       Q /= Q
       
    if Q == 1:
        p = 2
        while p < P:
            p *= 2
            ans -= 1

    else:
        ans = "impossible"

    if ans > 40:
        ans  = "impossible"

    print "Case #%d: %s" % (caseno + 1, ans)
