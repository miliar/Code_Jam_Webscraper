#!/usr/bin/python

from collections import deque

def get():
    dstx, dsty = map(int, raw_input().strip().split())
    if (dstx, dsty) == (0,0):
        return ''

    dirs = (('N', 0, 1), ('S', 0, -1), ('E', 1, 0), ('W', -1, 0))
    que = deque([(0, 0, 0)])
    last = {}
    last[(0,0)] = -1

    def path():
        p = []
        x, y = dstx, dsty
        while True:
            c, x, y = last[(x,y)]
            p.append(c)
            if (x,y) == (0,0):
                break
        return ''.join(reversed(p))

    while len(que):
        x, y, n = que.popleft()
        if (x, y) == (dstx, dsty):
            return path()
        n += 1
        #print (x,y)
        for c, dx, dy in dirs:
            nx = x + dx * n
            ny = y + dy * n
            if (nx, ny) in last:
                continue
            last[(nx,ny)] = (c, x, y)
            #print (x,y), c, (nx, ny)
            que.append((nx, ny, n))

n = input()
for x in xrange(n):
    print 'Case #%d: %s' % (x+1, get())
