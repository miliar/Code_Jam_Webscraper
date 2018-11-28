#!/usr/bin/env python


def solve(s):
    cakes, w = s.split(" ")
    w = int(w)
    cakes = list(cakes)
    n = len (cakes)
    k = 0
    for i in range(n-w+1):
        if cakes[i] == '-':
            k += 1
            for j in range (i, i+w):
                cakes[j] = ('+' if cakes[j] == '-' else '-')
    test = True
    for i in range (max(0,n-w), n):
        if cakes[i] == '-':
            test = False

    if test:
        return '%d' % k
    else:
        return 'IMPOSSIBLE'


if __name__ == "__main__":
    import sys
    l = sys.stdin.readlines()
    c = int(l[0])
    for i in range(1,c+1):
        sol = solve(l[i])
        print "Case #%d: %s" % (i, sol)

