# -*- coding: utf-8 -*-
def xor(a,b):
    return a^b
    
import sys
fin = sys.stdin
N = int(fin.readline())
for case in range(1,N+1):
    n = int(fin.readline())
    pile = map(int, fin.readline().split())
    if reduce(xor, pile) == 0:
        result = sum(pile) - min(pile)
    else:
        result = "NO"
    print "Case #%d: %s" % (case, result)
