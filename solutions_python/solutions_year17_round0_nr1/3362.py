# -*- coding: utf-8 -*-
import sys
rl = lambda: sys.stdin.readline().strip()


def flip(x, beg, end):
    xx = x[::]
    for i in range(beg, end):
        xx[i] = '+' if xx[i] == '-' else '-'
    return xx


T = int(rl())
for tcase in range(1, T + 1):
    state, k = rl().split()
    n, k = len(state), int(k)
    print >> sys.stderr, tcase, n, k
    state = [s for s in state]
    gt = ['+' for i in range(n)]
    seen, Q = set([''.join(state)]), [(state, 0)]
    ans = -1
    while Q:
        q, Q = Q[0], Q[1:]
        item, no = q
        if item == gt:
            ans = no
            break
        for i in range(0, n - k + 1):
            qq = flip(item, i, i + k)
            if ''.join(qq) not in seen:
                Q.append((qq, no + 1))
                seen.add(''.join(qq))
    if ans == -1:
        print 'Case #%d: IMPOSSIBLE' % (tcase)
    else:
        print 'Case #%d: %s' % (tcase, ans)
