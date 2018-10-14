#!/usr/bin/env python

import sys
import re

t = int(sys.stdin.readline().strip())


DIRS = [(-1, 0), (0, -1), (0, 1), (1, 0)]

for it in xrange(t):
    h, w = (int(i) for i in sys.stdin.readline().strip().split())

    alt = []
    for ih in xrange(h):
        row = [int(i) for i in sys.stdin.readline().strip().split()]
        assert len(row) == w, row
        alt.append(row)
    assert len(alt) == h, alt

    def calc_dir(ih, iw):
        neigh_alt = []
        for i,j in DIRS:
            if 0 <= ih+i < h and 0 <= iw+j < w:
                neigh_alt.append(alt[ih+i][iw+j])
            else:
                neigh_alt.append(sys.maxint)
        minalt = min(neigh_alt)
        if minalt < alt[ih][iw]:
            return neigh_alt.index(minalt)
        else:
            return -1

    dir = [[calc_dir(ih, iw) for iw in xrange(w)] for ih in xrange(h)]
    bas = [[0 for iw in xrange(w)] for ih in xrange(h)]

    def receives(curr, d):
        src = (curr[0]+d[0], curr[1]+d[1])
        if 0 <= src[0] < h and 0 <= src[1] < w:
            srcdiridx = dir[src[0]][src[1]]
            if srcdiridx != -1:
                srcdir = DIRS[srcdiridx]
                return srcdir[0]+d[0] == 0 and srcdir[1]+d[1] == 0
        return False

    latestpos = (0,0)
    done = False
    curbas = 1

#    for r in dir:
#        print str(r)

    while not done:
        heads = set([latestpos])
        bas[latestpos[0]][latestpos[1]] = curbas

        while heads:
            curr = heads.pop()
            assert bas[curr[0]][curr[1]] == curbas
#            print curr
            curdir = dir[curr[0]][curr[1]]
            if curdir != -1:
                curdir = DIRS[curdir]
                examinedirs = [(curr[0]+curdir[0], curr[1]+curdir[1])]
            else:
                examinedirs = []
            examinedirs.extend([(curr[0]+d[0], curr[1]+d[1]) for d in DIRS
                                            if receives(curr, d)])
#            print "exam", examinedirs
            for neigh in set(examinedirs):
                nbas = bas[neigh[0]][neigh[1]]
                if nbas:
                    assert nbas == curbas, "%d == %d" % (nbas, curbas)
                else:
                    bas[neigh[0]][neigh[1]] = curbas
#                    print "add", neigh
                    heads.add(neigh)
        curbas += 1

        while bas[latestpos[0]][latestpos[1]]:
            nextr, nextc = latestpos[0], latestpos[1]+1
            if nextc >= w:
                nextc = 0
                nextr += 1
                if nextr >= h:
                    done = True
                    break
            latestpos = (nextr, nextc)


    print "Case #%d:" % (it+1)
    for r in bas:
        print ' '.join([chr(ord('a')-1+i) for i in r])








