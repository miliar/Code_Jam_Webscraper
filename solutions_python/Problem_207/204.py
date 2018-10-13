#!/usr/bin/env python

def solve_simple(n1, n2, n3):
    l = [(n1, 'R'), (n2, 'Y'), (n3, 'B')]
    l.sort()
    s = n1 + n2 + n3
    if 2*l[2][0] > s:
        return 'IMPOSSIBLE'
    soltab = [l[2][1]] * s
    nxt = l[1][1]
    i = s-1
    k = l[0][0]
    while i > 2*(l[2][0]-1):
        soltab[i] = nxt
        if nxt == l[0][1]:
            k -= 1
            nxt = l[1][1]
        elif k > 0:
            nxt = l[0][1]
        i -= 1
    i -= 1
    while i > 0:
        soltab[i] = nxt
        if nxt == l[0][1]:
            k -= 1
            nxt = l[1][1]
        elif k > 0:
            nxt = l[0][1]
        i -= 2
    return ''.join(soltab)


if __name__ == "__main__":
    import sys
    l = sys.stdin.readlines()
    c = int(l[0])
    for i in range(1,c+1):
        n, r, o, y, g, b, v = [int(k) for k in l[i].split()]
        if n == r + y + b:
            sol = solve_simple(r, y, b)
        else:
            sol = 'Unimplemented'

        print "Case #%d: %s" % (i, sol)
