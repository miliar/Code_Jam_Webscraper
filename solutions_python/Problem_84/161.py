#!/usr/bin/python

def doit():
    r, c = map(int, raw_input().strip().split())
    tag = {}
    blue = []
    for x in xrange(r):
        line = raw_input().strip()
        for y in xrange(c):
            if line[y] == '#':
                tag[(x,y)] = 0
                blue.append((y,x))


    if len(blue) % 4:
        return False

    def ok(x, y):
        # must be in range
        # and must be blue and not yet been redded
        return x < r and y < c and (x,y) in tag and tag[(x,y)] == 0

    htid = [0]
    def red(x, y):
        if not ok(x,y+1) or not ok(x+1,y) or not ok(x+1,y+1):
            return False
        htid[0] += 1
        tid = htid[0]
        tag[(x,y)] = tid
        tag[(x+1,y)] = tid
        tag[(x,y+1)] = tid
        tag[(x+1,y+1)] = tid
        return True

    blue.sort()
    for y, x in blue:
        if tag[(x,y)]:
            continue
        if not red(x, y):
            return False

    matrix = []
    for x in xrange(r):
        matrix.append(['.'] * c)

    for y,x in blue:
        if tag[(x,y)] == 0:
            continue
        matrix[x][y] = '/'
        matrix[x+1][y] = '\\'
        matrix[x][y+1] = '\\'
        matrix[x+1][y+1] = '/'
        tag[(x,y)] = 0
        tag[(x+1,y)] = 0
        tag[(x,y+1)] = 0
        tag[(x+1,y+1)] = 0

    for x in xrange(r):
        print ''.join(matrix[x])

    return True


n = input()
for x in xrange(n):
    print 'Case #%d:' % (x+1)
    if not doit():
        print 'Impossible'
