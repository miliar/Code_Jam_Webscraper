# -*- coding: utf-8 -*-

from sys import stdin

dirs = ((-1, 0), (0, -1), (0, 1), (1, 0))

def main():
    h, w = map(int, stdin.readline().split())
    lines = [map(int, stdin.readline().split()) for _ in xrange(h)]
    sol = [[None]*w for _ in xrange(h)]
    def g(x, y):
        if sol[x][y] is None:
            b, bv = (x, y), lines[x][y]
            for dx, dy in dirs:
                if 0 <= x + dx < h and 0 <= y + dy < w:
                    if lines[x+dx][y+dy] < bv:
                        b = (x+dx, y+dy)
                        bv = lines[x+dx][y+dy]
            if b != (x, y):
                b = g(b[0], b[1])
            sol[x][y] = b
        return sol[x][y]
    def gl(p, dd={}, c=[ord('a')]):
        if p not in dd:
            dd[p] = chr(c[0])
            c[0] += 1
        return dd[p]
    return "".join("\n" + " ".join(gl(g(x,y)) for y in xrange(0, w)) for x in xrange(0, h))

tno = int(stdin.readline())
for i in xrange(0, tno):
    print "Case #%d: %s"%(i+1, main())
