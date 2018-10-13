# -*- coding: utf-8 -*-

import sys, itertools

def ac(x,y,rows):
    H = len(rows)
    W = len(rows[0])
    if x >= W or y >= H or x < 0 or y < 0:
        return None
    else:
        return rows[y][x]

def flow(x,y,rows,resrows,csn):
    #print 'flow: ',x,y,csn,resrows[y][x]

    if resrows[y][x] != None:
        return resrows[y][x]

    ajs = []
    ajs.append((ac(x,y-1,rows),'n',0,-1))
    ajs.append((ac(x,y+1,rows),'s',0,+1))
    ajs.append((ac(x+1,y,rows),'e',+1,0))
    ajs.append((ac(x-1,y,rows),'w',-1,0))

    #print "ajs", x,y,ajs

    ma,md,mxd,myd = 100000,None,None,None
    for a,d,xd,yd in ajs:
        if a==None:
            continue
        if a<ma or (a==ma and 'nwes'.index(d) < 'nwes'.index(md)):
            ma,md,mxd,myd = a,d,xd,yd
    ca = ac(x,y,rows)
    
    #print 'flow calc:', ca,ma,md,x,y,resrows[y][x],csn

    if ma >= ca: # found new sink?
        #print 'new sink:', x,y,csn
        resrows[y][x] = csn
        return csn
    else:
        sn = flow(x+mxd,y+myd,rows,resrows,csn)
        #print 'non-sink:',x,y
        resrows[y][x] = sn
        return sn
    

def calc(rows,H,W):
    resrows = []
    for i in xrange(H):
        resrows.append([None] * W)
    
    ss = 'abcdefghijklmnopqrstuvwxyz'

    #print 'w h: ', W,H
    csn = 'a'
    x,y = 0,0
    while y < H:
        sn = flow(x,y,rows,resrows,csn)
        if sn==csn and csn != 'z':
            csn = ss[ss.index(csn)+1]
            #csn += 1
        
        if x < W-1:
            x += 1
        else:
            x = 0
            y += 1
    
    return resrows # FIXME aakkosta sink-numerot



fn = sys.argv[1]
def gen_lines(fn):
    for lineRaw in open(fn, 'r').readlines():
        line = lineRaw[0:-1]
        yield line


gl = gen_lines(fn)

gl.next()

i = 1
while True:
    try:
        line = gl.next()
        H,W = [int(sd) for sd in line.split(' ')]
        rows = []
        hc = 0
        while hc < H:
            line = gl.next()
            row = [int(sn) for sn in line.split(' ')]
            rows.append(row)
            assert len(row) == W
            hc += 1

        # calculate
        print "Case #%d:" % (i,)
        for row in calc(rows,H,W):
            rs = [str(o) for o in row]
            print ' '.join(rs)

        i += 1
    except StopIteration:
        break
