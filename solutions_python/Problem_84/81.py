T = int(raw_input())
for t in xrange(T):
    R, C = [int(x) for x in raw_input().split(' ')]
    tiles = []
    for r in xrange(R):
        tiles.append([])
        for ch in raw_input().rstrip():
            tiles[r].append(ch)
    for r in xrange(R - 1):
        for c in xrange(C - 1):
            if tiles[r][c] != '#': continue
            if tiles[r][c+1] != '#': continue
            if tiles[r+1][c] != '#': continue
            if tiles[r+1][c+1] != '#': continue
            tiles[r][c] = '/'
            tiles[r][c+1] = '\\'
            tiles[r+1][c] = '\\'
            tiles[r+1][c+1] = '/'
    print "Case #%d:" % (t + 1)
    impossible = False
    for r in xrange(R):
        if '#' in tiles[r]:
            impossible = True
            break
    if impossible:
        print 'Impossible'
    else:
        for r in xrange(R):
            print ''.join(tiles[r])

