import itertools, copy
s = open('/tmp/t.txt','r').readlines()
T = int(s[0])
k= 1
for x in xrange(T):
    H,W = map(int, s[k].split())
    k+=1
    the_map = map(lambda x: map(int,x.strip().split()),s[k:k+H])
    k+=H

    new_map = [[0 for xx in xrange(W)] for yy in xrange(H)]
    new_map_rel = [[False for xx in xrange(W)] for yy in xrange(H)]
    new_map_dir = [[None for xx in xrange(W)] for yy in xrange(H)]
    sinks = []
    for i in xrange(H):
        for j in xrange(W):
            i1,j1 = max(0,i-1),j
            i2,j2 = i,min(W-1,j+1)
            i3,j3 = min(H-1,i+1),j
            i4,j4 = i,max(0,j-1)
            if     the_map[i][j]<=the_map[i1][j1] \
               and the_map[i][j]<=the_map[i2][j2] \
               and the_map[i][j]<=the_map[i3][j3] \
               and the_map[i][j]<=the_map[i4][j4]:
                   sinks.append((i,j))
    ii = 1
    for (i,j) in sinks:
        new_map[i][j] = ii
        ii += 1

    for i in xrange(H):
        for j in xrange(W):
            neighbours = []
            if i>0 and the_map[i-1][j]<the_map[i][j]: # N
                neighbours.append((4, the_map[i-1][j], i-1, j))
            if j>0 and the_map[i][j-1]<the_map[i][j]: # W
                neighbours.append((3, the_map[i][j-1],i, j-1))
            if j<W-1 and the_map[i][j+1]<the_map[i][j]: # E
                neighbours.append((2, the_map[i][j+1],i, j+1))
            if i<H-1 and the_map[i+1][j]<the_map[i][j]: # S
                neighbours.append((1, the_map[i+1][j],i+1, j))
            if neighbours:
                neighbours.sort(lambda x,y: 1 if x[1]>y[1] or (x[1]==y[1] and x[0]<y[0]) else -1)
                _1, _2, ni,nj = neighbours[0]
                new_map_dir[i][j]=(ni,nj)

    fl = True
    while fl:
        fl = False
        for i in xrange(H):
            for j in xrange(W):
                if new_map[i][j]==0 and new_map_dir[i][j]:
                    ni,nj = new_map_dir[i][j]
                    if new_map[ni][nj]!=0:
                        fl=True
                        new_map[i][j] = new_map[ni][nj]


    ii = ord('a')
    def replace_all(val, new_val):
        for i in xrange(H):
            for j in xrange(W):
                if new_map[i][j]==val:
                    new_map[i][j]=new_val
                    new_map_rel[i][j] = True

    for i in xrange(H):
        for j in xrange(W):
            if not new_map_rel[i][j]:
                replace_all(new_map[i][j], ii)
                ii +=1
    print "Case #%s:" %(x+1,)
    print '\n'.join(map(lambda line:' '.join(map(chr,line)),new_map))
