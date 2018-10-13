#!/usr/bin/python

T = input()
for case in xrange(1,T+1):
    xy = raw_input()
    x,y = [int(a) for a in xy.split()]
    tiles = []
    for i in xrange(x):
        l = raw_input()
        l = [a for a in l]
        tiles.append(l)
    case_possible = True
    for i in xrange(x):
        if not case_possible:
            break
        for j in xrange(y):
            if tiles[i][j] == '#':
                possible = True
                if j+1 < y and tiles[i][j+1] == '#':
                    pass
                else:
                    possible = False
                if i+1 < x and tiles[i+1][j] == '#':
                    pass
                else:
                    possible = False
                if i+1 < x and j+1 < y and tiles[i+1][j] == '#':
                    pass
                else:
                    possible = False
                if possible:
                    tiles[i][j] = '/'
                    tiles[i][j+1] = '\\'
                    tiles[i+1][j] = '\\'
                    tiles[i+1][j+1] = '/'
                else:
                    case_possible = False
    print "Case #%d:"%case
    if not case_possible:
        print "Impossible"
    else:
        for t in tiles:
            print "%s"%(''.join(t))

