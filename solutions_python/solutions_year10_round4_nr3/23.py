fin = open('in', 'r')
test_count = int(fin.readline().rstrip())

dx = 101
dy = 101

for tn in xrange(test_count):
    r = int(fin.readline().rstrip())
    
    p = [[0]*dx for i in xrange(dy)]
    
    for i in xrange(r):
        x1, y1, x2, y2 = [int(x) for x in fin.readline().rstrip().split()]
        for x in xrange(x1, x2+1):
            for y in xrange(y1, y2+1):
                p[x][y]=1

    count = 0
    for x in xrange(0, dx):
        for y in xrange(0, dy):
            if p[x][y] == 1:
                count += 1

    round = 0
    while count > 0:
        round += 1
        q = [[0]*dx for i in xrange(dy)]
        for x in xrange(0, dx):
            for y in xrange(0, dy):
                q[x][y] = 1 if (p[x][y] and ((x > 0 and p[x-1][y]) or (y > 0 and p[x][y-1]))) or (x > 0 and p[x-1][y] and y > 0 and p[x][y-1]) else 0
        p = q

        count = 0
        for x in xrange(0, dx):
            for y in xrange(0, dy):
                if p[x][y] == 1:
                    count += 1

    print 'Case #%d: %d' % (tn+1, round)
