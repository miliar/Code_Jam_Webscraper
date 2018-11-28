import sys

def water_direction(hmap, x, y, W, H):
    pos = []
    curr = hmap[y][x]
    if y > 0: pos.append((x, y-1))
    if x > 0: pos.append((x-1, y))
    if x < W-1: pos.append((x+1, y))
    if y < H-1: pos.append((x, y+1))
    if not pos:
        return x, y
    levels = [hmap[cy][cx] for cx, cy in pos]
    m = min(levels)
    if m >= curr:
        return x, y
    else:
        for i, l in enumerate(levels):
            if l == m:
                return pos[i]

alphabet = "abcdefghijklmnopqrstuvwxyz"
f = open(sys.argv[1], "r")
line = f.readline()
T = int(line.strip())
for t in xrange(T):
    line = f.readline()
    H, W = map(lambda x: int(x), line.split())
    hmap = []
    basins = []
    bcount = 0
    for h in xrange(H):
        line = f.readline()
        hmap.append( map(lambda x: int(x), line.split()) )
        basins.append([-1 for i in xrange(W)])
    for h in xrange(H):
        for w in xrange(W):
            if basins[h][w] > -1:
                continue
            path = [(w, h)]
            xp, yp = w, h
            bfind = 0
            while True:
                x, y = water_direction(hmap, xp, yp, W, H)
                if x == xp and y == yp:
                    #sink
                    bfind = bcount
                    bcount += 1
                    break
                bt = basins[y][x]
                if bt > -1:
                    bfind = bt
                    break                
                path.append((x, y))
                xp, yp = x, y
            for x, y in path:
                basins[y][x] = bfind
    print "Case #%d:" % (t+1)
    for row in basins:
        print ' '.join([alphabet[i] for i in row])
