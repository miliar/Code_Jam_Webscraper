#!/usr/bin/env python
# chteo@gcj09::0::B

from sys import argv


SINK  = 0
UP    = 1
LEFT  = 2
DOWN  = 3
RIGHT = 4

def floodfill(a,y,x,color,cmap,amap,fmap,H,W):
    Q = [(x,y,a)]
    while len(Q) > 0:
        x,y,a = Q.pop(0)
        #print x,y,color
        cmap[y][x] = color
        # up
        if y-1 >= 0 and cmap[y-1][x] == 0:
            if amap[y-1][x] > a and (fmap[y-1][x] == DOWN):
                Q.append((x,y-1,amap[y-1][x]))
        # left
        if x-1 >= 0 and cmap[y][x-1] == 0:
            if amap[y][x-1] > a and (fmap[y][x-1] == RIGHT):
                Q.append((x-1,y,amap[y][x-1]))
        # down
        if y+1 < H and cmap[y+1][x] == 0:
            if amap[y+1][x] > a and (fmap[y+1][x] == UP):
                Q.append((x,y+1,amap[y+1][x]))
        # right
        if x+1 < W and cmap[y][x+1] == 0:
            if amap[y][x+1] > a and (fmap[y][x+1] == LEFT): 
                Q.append((x+1,y,amap[y][x+1]))


# determine the flow direction of each cell
def get_flow_dir(H,W,amap):
    fmap = [[0]*W for i in range(H)]
    for y in xrange(H):
        for x in xrange(W):
            lowest = amap[y][x]
            fmap[y][x] = SINK
            if y-1 >= 0:
                if amap[y-1][x] < lowest:
                    lowest = amap[y-1][x]
                    fmap[y][x] = UP
            if x-1 >= 0:
                if amap[y][x-1] < lowest:
                    lowest = amap[y][x-1]
                    fmap[y][x] = LEFT
            if x+1 < W:
                if amap[y][x+1] < lowest:
                    lowest = amap[y][x+1]
                    fmap[y][x] = RIGHT
            if y+1 < H:
                if amap[y+1][x] < lowest:
                    lowest = amap[y+1][x]
                    fmap[y][x] = DOWN
    return fmap



def get_drainage(H,W,M):
    amap = [map(eval,m.split()) for m in M]
    fmap = get_flow_dir(H,W,amap)

#     print "fmap"
#     for l in fmap:
#         print l

#     print "amap"
#     for l in amap:
#         print l

    cmap = [[0]*W for i in range(H)]
    C = [(amap[y][x],y,x) for y in xrange(H) for x in xrange(W)]
    
    color = 1
    for a,y,x in sorted(C): 
        if cmap[y][x] == 0:
#             # bug bug
#             if color > MAX_BASINS:
#                 print '*'*20,'   ERROR   ','*'*20
            floodfill(a,y,x,color,cmap,amap,fmap,H,W)
            color += 1
    
    # relabel map
    D = {}
    label = 'a'
    for y in xrange(H):
        for x in xrange(W):
            if cmap[y][x] not in D:
                D[cmap[y][x]] = label
                label = chr(ord(label)+1)
    # format map
    str = ''
    for row in cmap:
        str += D[row[0]]
        for c in row[1:]:
            str += ' '+D[c]
        str += '\n'
    return str
            
                

f = open(argv[1])
MAX_BASINS = 26
if len(argv) > 2:
    MAX_BASINS = int(argv[2])
    print 'max # of basins =', MAX_BASINS

T = int(f.readline().strip())

for i in xrange(T):
    H,W = map(eval,f.readline().strip().split())
    M = []
    for j in xrange(H):
        l = f.readline().strip()
        M.append(l)
    drainage_str = get_drainage(H,W,M)
    print 'Case #%d:' % (i+1)
    print drainage_str,
    
