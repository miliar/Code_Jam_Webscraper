

import sys

data = iter(sys.stdin)
cases = int(data.next().rstrip())
for c in xrange(cases):
    size = data.next().rstrip().split(' ')
    H = int(size[0])
    W = int(size[1])
    field = [[int(a) for a in data.next().rstrip().split(' ')] for _ in xrange(H)]

    worked = True

    for y in xrange(H):
        for x in xrange(W):
            h = field[y][x]
            # Check column
            col = True
            for iy in xrange(H):
                if field[iy][x] > h:
                    col = False
                    break
            # Check row
            row = True
            for ix in xrange(W):
                if field[y][ix] > h:
                    row = False
                    break
            worked = col or row
            if not worked:
                break
        if not worked:
            break
    if worked:
        print "Case #{}: {}".format(c + 1, 'YES')
    else:
        print "Case #{}: {}".format(c + 1, 'NO')



