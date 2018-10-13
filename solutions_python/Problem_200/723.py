#!/usr/bin/env python
# -*- coding utf-8 -*-

import sys
import math

def check(N, sl, t):
    #print("N: ",N)
    l = sl
    v = N // (10**(l-1))
    if len(str(N)) != sl:
        v = 0

    #print(v, t)
    if t <= v:
        if l == 1:
            return v

        if len(str(N)) != sl:
            nn = N
        else:
            nn = int(str(N)[1:])
        ret = check(int(nn), sl-1, v)
        #print(ret)
        if ret is None:
            v -= 1

            if t > v:
                return None

            ret = v*(10**(l-1))
            if l >= 2:
                s = str(9)*(l-1)
                if s != "":
                    ret += int(s)
            return ret

        return int(str(v) + str(ret))
    else:
        return None


T = int(sys.stdin.readline().strip())
c = 1
while True:
    l = sys.stdin.readline().strip()
    if l == "":
        break
    N = int(l)

    result = check(N, len(str(N)), 0)

    print("Case #%d: %s" % (c, result))

    c += 1
