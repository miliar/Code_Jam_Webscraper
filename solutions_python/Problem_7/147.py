#!/usr/bin/env python
# Google Code Jam 2008
# Online Round 1B
# Problem A
# Crop Triangles

import math

def getPoints(n, A, B, C, D, x0, y0, M):
    pts = []
    X = x0
    Y = y0
#    print X, Y
    pts.append((X, Y))
    for i in xrange(1, n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
#        print X, Y
        pts.append((X, Y))
    return pts


def main():
    N = int(raw_input())
    for case in xrange(N):
        count = 0
        n, A, B, C, D, x0, y0, M = map(int, raw_input().split())
#        print n, A, B, C, D, x0, y0, M
        p = getPoints(n, A, B, C, D, x0, y0, M)
#        import pprint
#        pprint.pprint(p)
        for i in xrange(len(p)):
            for j in xrange(i + 1, len(p)):
                for k in xrange(j + 1, len(p)):

                        ptr = ((p[i][0] + p[j][0] + p[k][0]) / 3.0, (p[i][1] + p[j][1] + p[k][1]) / 3.0)
                        if ptr[0] - math.floor(ptr[0]) == 0 and ptr[1] - math.floor(ptr[1]) == 0:
                            count += 1

        print "Case #%d: %d" % (case + 1, count)
                            

if __name__ == "__main__":
    main()
