# -*- coding: utf-8 -*-

t = int(raw_input())
for case in xrange(t):
    n = int(raw_input())
    allwires = []
    inters = []
    points = 0
    for i in xrange(n):
        ai, bi = [int(x) for x in raw_input().split(' ')]
        if ai == bi:
            for conns in inters:
                a, b = conns
                if (a > ai and b < ai) or (b > ai and a < ai):
                    points += 1
        else:
            for conns in allwires:
                a, b = conns
                if (ai > a and bi < b) or (ai < a and bi > b):
                    points += 1
            inters.append((ai, bi))
        allwires.append((ai, bi))
    print 'Case #%d: %d' % (case + 1, points)
