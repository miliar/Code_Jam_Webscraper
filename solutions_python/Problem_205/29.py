#!/usr/bin/env python

import sys
ls = sys.stdin.readlines()[1:]
C = 1
for l in ls:
    hd, ad, hk, ak, buff, debuff = [int(x) for x in l.split()]
    seen = set()
    seen.add((hd, ad, hk, ak))
    q = [(0, (hd, ad, hk, ak))]
    ans = -1
    idx = 0
    while idx < len(q) and ans == -1:
        d, x = q[idx]
        idx += 1
        if x[2] <= 0:
            ans = d
            break
        turns = [(x[0] - (x[3] if (x[2] - x[1]) > 0 else 0), x[1], x[2] - x[1], x[3]),
                 (hd - x[3], x[1], x[2], x[3])]
        if x[3] > 0:
            turns.append((x[0] - max(0, x[3] - debuff), x[1], x[2], max(0, x[3] - debuff)))

        if x[1] < x[2]:
            turns.append((x[0] - x[3], x[1] + buff, x[2], x[3]))

        for turn in turns:
            if turn[0] > 0 and turn not in seen:
                seen.add(turn)
                q.append((d + 1, turn))

    if ans == -1:
        print "Case #%d: IMPOSSIBLE" % C
    else:
        print "Case #%d: %d" % (C, ans)
    C += 1
