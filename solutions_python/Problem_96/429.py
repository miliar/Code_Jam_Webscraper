# -*- coding: utf-8 -*-
import sys
import math

stin = sys.stdin
stin.readline() # 1行読み飛ばし

for no,line in enumerate(stin.readlines()):
    nspt = map(int, line.split())
    (n,s,p) = nspt[0:3]
    t = nspt[3:]
    ans = 0
    for point in sorted(t, reverse=True):
        rem = point % 3
        avg = point / 3
        if avg >= p:
            ans += 1
            continue
        if (rem == 1 or rem == 2) and avg == p-1:
            ans += 1
            continue
        if s == 0 : break
        if (rem == 0 and avg == p-1 and avg > 0) or (rem == 2 and avg == p-2):
            s -= 1
            ans += 1
            continue
        break

    print("Case #%d: %d" % (no+1, ans))
