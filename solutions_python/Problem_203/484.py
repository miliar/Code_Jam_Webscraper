import sys

T = int(sys.stdin.readline())

for t in xrange(T):
    R, C = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    # cake = [sys.stdin.readline().strip() for r in xrange(R)]
    cake = [list(sys.stdin.readline().strip()) for r in xrange(R)]

    for i in xrange(R):
        child = cake[i][0]
        for j in xrange(1, C):
            if child != '?' and cake[i][j] == '?':
                cake[i][j] = child
            child = cake[i][j]

    cake = [list(reversed(row)) for row in cake]

    for i in xrange(R):
        child = cake[i][0]
        for j in xrange(1, C):
            if child != '?' and cake[i][j] == '?':
                cake[i][j] = child
            child = cake[i][j]

    cake = [list(reversed(row)) for row in cake]

    row = cake[0]
    for i in xrange(1, R):
        if row[0] != '?' and cake[i][0] == '?':
            cake[i] = row
        row = cake[i]

    cake = list(reversed(cake))

    row = cake[0]
    for i in xrange(1, R):
        if row[0] != '?' and cake[i][0] == '?':
            cake[i] = row
        row = cake[i]

    cake = list(reversed(cake))

    print "Case #%d:" % (t + 1)
    for row in cake:
        print ''.join(row)