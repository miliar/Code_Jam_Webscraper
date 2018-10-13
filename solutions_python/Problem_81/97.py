#!/usr/bin/python

def doit():
    n = input()
    matrix = []
    for x in xrange(n):
        matrix.append(raw_input().strip())
    
    wp = [0] * n
    for x in xrange(n):
        won, games = 0, 0
        for y in xrange(n):
            a = matrix[x][y]
            if a == '.':
                continue
            games += 1
            if a == '1':
                won += 1
        wp[x] = won / float(games)

    def getwp(x, y):
        won, games = 0, 0
        for i in xrange(n):
            if i == x:
                continue
            a = matrix[y][i]
            if a == '.':
                continue
            games += 1
            if a == '1':
                won += 1
        return won / float(games)

    owp = [0] * n
    for x in xrange(n):
        now, games = 0, 0
        for y in xrange(n):
            a = matrix[x][y]
            if a == '.':
                continue
            games += 1
            now += getwp(x, y)
        owp[x] = now / float(games)

    oowp = [0] * n
    for x in xrange(n):
        now, games = 0, 0
        for y in xrange(n):
            a = matrix[x][y]
            if a == '.':
                continue
            games += 1
            now += owp[y]
        oowp[x] = now / float(games)

    for x in xrange(n):
        print '%.12f' % (.25 * wp[x] + .5 * owp[x] + .25 * oowp[x])


n = input()
for x in xrange(n):
    print 'Case #%d:' % (x+1)
    doit()
