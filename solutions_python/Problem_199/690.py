#!/usr/bin/env python
# -*- coding utf-8 -*-

import sys


#def check(S, K):
#    try:
#        i = S.index('-')
#    except ValueError:
#        return 0
#
#    ss = S[i:]
#
#    if len(ss) < K:
#        return None
#
#    # flip
#    for a in range(K):
#        if ss[a] == "-":
#            ss[a] = "+"
#        else:
#            ss[a] = "-"
#
#    subresult = check(ss, K)
#    if subresult is None:
#        return None
#    else:
#        return 1 + subresult
def check(S, K):
    ss = S
    current = 0
    while True:
        try:
            i = ss.index('-')
        except ValueError:
            return current
    
        ss = ss[i:]
    
        if len(ss) < K:
            return None
    
        # flip
        for a in range(K):
            if ss[a] == "-":
                ss[a] = "+"
            else:
                ss[a] = "-"
    
        current += 1


T = int(sys.stdin.readline().strip())
c = 1
while True:
    l = sys.stdin.readline().strip()
    if l == "":
        break
    s, n = l.split(" ")

    S = list(s)
    N = int(n)

    result = check(S, N)

    if result is not None:
        print("Case #%d: %s" % (c, result))
    else:
        print("Case #%d: IMPOSSIBLE" % c)

    c += 1
