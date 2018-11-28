# ertug (Ertug Karamatli)

import sys
import re
from math import floor

f = file(sys.argv[1])

ln = 0

T = 0

#read
maps = []
mapstart = False
cH = 0
for line in f:
    line = line.strip()
    if line == '': continue
    if ln == 0:
        T = int(line)
    elif mapstart == False:
        H, W = line.split(' ')
        H = int(H)
        W = int(W)
        cH = 0
        cmap = []
        if H != 0 or W != 0: mapstart = True
    elif mapstart:
        cmap.append(line.split(' '))
        cH += 1

    if ln != 0 and cH == H:
        mapstart = False
        maps.append(cmap)

    ln += 1


def label(p, pmap, lmap, curlabel):
    curlabel2 = int(curlabel)
    for i in xrange(len(pmap)):
        for j in xrange(len(pmap[0])):
            c = pmap[i][j]
            if type(c) == list:
                if p in c:
                    c.remove(p)
                    pmap[i][j] = curlabel2
                    for path in c:
                        label(path, pmap, lmap, curlabel2)
cn = 1
for cmap in maps:
    pmap = []
    lmap = []
    for i in xrange(len(cmap)):
        pmap.append([])
        lmap.append([])
        for j in xrange(len(cmap[0])):
            pmap[i].append([])
            lmap[i].append('')
            cmap[i][j] = int(cmap[i][j])

    pid = 0
    for i in xrange(len(cmap)):
        for j in xrange(len(cmap[0])):
            mapcont = True
            curcell = [i, j]
            while mapcont:
                ccx = curcell[0]
                ccy = curcell[1]
                curalti = cmap[ccx][ccy]
                if ccx - 1 >= 0:
                    nn = cmap[ccx - 1][ccy]
                else:
                    nn = sys.maxint
                if ccy - 1 >= 0:
                    nw = cmap[ccx][ccy - 1]
                else:
                    nw = sys.maxint
                if ccy + 1 < len(cmap[ccx]):
                    ne = cmap[ccx][ccy + 1]
                else:
                    ne = sys.maxint
                if ccx + 1 < len(cmap):
                    ns = cmap[ccx + 1][ccy]
                else:
                    ns = sys.maxint

                pmap[ccx][ccy].append(pid)
                minalti = min(nn,nw,ne,ns)
                if curalti > minalti:
                    if nn == minalti and not pid in pmap[ccx - 1][ccy]:
                        curcell = [ccx - 1, ccy]
                    elif nw == minalti and not pid in pmap[ccx][ccy - 1]:
                        curcell = [ccx, ccy - 1]
                    elif ne == minalti and not pid in pmap[ccx][ccy + 1]:
                        curcell = [ccx, ccy + 1]
                    elif ns == minalti and not pid in pmap[ccx + 1][ccy]:
                        curcell = [ccx + 1, ccy]
                    else:
                        break
                else:
                    break

                #mapcont = False

            pid += 1

    curlabel = 1
    for p in xrange(pid):
        label(p, pmap, lmap, curlabel)
        curlabel += 1

    #print 'Case #%s: %s' % (cn, c)

    lset = set()
    for i in xrange(len(pmap)):
        for j in xrange(len(pmap[0])):
            lset.add(pmap[i][j])

    ldict = {}
    newlabel = 'a'
    for l in sorted(lset):
        ldict.update({l: newlabel})
        newlabel = chr(ord(newlabel)+1)

    print 'Case #%s:' % cn
    for i in xrange(len(pmap)):
        for j in xrange(len(pmap[0])):
            sys.stdout.write(ldict[pmap[i][j]])
            if j != len(pmap[0]) - 1: sys.stdout.write(' ')
        sys.stdout.write('\n')

    cn += 1

