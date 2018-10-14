def move(stack, p, cost):
    if stack:
        q = stack[-1]
        d = min(cost, abs(p - q))
        return p + d * cmp(q, p)

def solve(s):
    bt = s.split()
    n = bt.pop(0)
    col = bt[::2]
    pos = map(int, bt[1::2])
    oo = [p for x, p in reversed(zip(col, pos)) if x == 'O']
    bb = [p for x, p in reversed(zip(col, pos)) if x == 'B']

    t = 0
    po, pb = 1, 1
    for x, p in zip(col, pos):
        if x == 'O':
            cost = abs(p - po) + 1
            po = p
            pb = move(bb, pb, cost)
            oo.pop()
        else:
            cost = abs(p - pb) + 1
            pb = p
            po = move(oo, po, cost)
            bb.pop()
        t += cost
    return t

def main(L):
    for t in range(1, 1 + int(L[0])):
        print 'Case #%d: %d' % (t, solve(L[t]))

import sys
main(list(sys.stdin))
