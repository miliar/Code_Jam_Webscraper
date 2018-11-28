#!/usr/bin/python

import math
import numpy as np

f = open("A-small-attempt0.in", "r")

T = int(f.readline())

out = open("A-small.out", "w")
outstr = "Case #%d: %d\n"


for i in range(T):
    r, t = [int(x) for x in f.readline().split()]
    
    n = ((1 - 2*r) + ((2*r-1)**2 + 8*t) ** 0.5) / 4.0

    cand = math.floor(n)

    paint = 2*r*cand + cand*(2*cand - 1)
    if paint > t:
        final = cand-1

    else:
        tmp = cand+1
        paint2 = 2*r*tmp + tmp*(2*tmp-1)
        if paint2 <= t:
            final = tmp
        else:
            final = cand

    out.write(outstr % (i+1, final))

out.close()
