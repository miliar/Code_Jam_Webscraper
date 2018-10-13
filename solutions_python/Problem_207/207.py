#!/usr/bin/python

def solve(case_no):
    n, r, o, y, g, b, v = map(int, raw_input().split())
    if max(r, y, b) * 2 > n:
        ans = 'IMPOSSIBLE'
    else:
        ring = []
        c, pc = None, None
        for i in xrange(n):
            if pc is None:
                if r == max(r, y, b):
                    c = 'R'
                    r -= 1
                elif y == max(r, y, b):
                    c = 'Y'
                    y -= 1
                elif b == max(r, y, b):
                    c = 'B'
                    b -= 1
            elif pc == 'R':
                if y > b:
                    c = 'Y'
                    y -= 1
                else:
                    c = 'B'
                    b -= 1
            elif pc == 'Y':
                if r > b:
                    c = 'R'
                    r -= 1
                else:
                    c = 'B'
                    b -= 1
            elif pc == 'B':
                if r > y:
                    c = 'R'
                    r -= 1
                else:
                    c = 'Y'
                    y -= 1
            ring.append(c)
            pc = c
        if ring[n-1] == ring[0]:
            for i in xrange(n-1, 0, -1):
                c = ring[i]
                ring[i] = ring[i-1]
                ring[i-1] = c
                if ring[i-1] != ring[i-2]:
                    break
        ans = ''.join(ring)
    print 'Case #%d: %s' % (case_no, ans)

t = int(raw_input())
for case_no in xrange(1, t+1):
    solve(case_no)
