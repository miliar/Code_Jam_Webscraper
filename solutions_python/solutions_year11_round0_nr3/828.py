#!/usr/bin/env python

import operator

def f(bag1, bag2, candy):
    if candy:
        c = candy[0]
        #put the candy in bag1
        n1 = f(bag1 + [c], bag2, candy[1:])
        #put the candy in bag2
        n2 = f(bag1, bag2 + [c], candy[1:])
        return max(n1,n2)
    else:
        b1 = reduce(operator.xor, bag1)
        b2 = reduce(operator.xor, bag2)
        if b1 and b1 == b2:
            return max(sum(bag1), sum(bag2))
        else:
            return 0
    
cases = int(raw_input())
for case in range(cases):
    t = int (raw_input())
    candy = map(int, raw_input().split(' '))
    
    r = f([0], [0], candy)
    
    if r == 0:
        print "Case #%d: NO" % (case + 1)
    else:
        print "Case #%d: %s" % (case + 1, r)
