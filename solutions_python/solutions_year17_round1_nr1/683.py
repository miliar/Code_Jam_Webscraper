def solve():
    R, C = map(int, raw_input().strip().split())
    cake = [['?']*C for i in xrange(R)]
    for i in xrange(R):
        row = raw_input()
        for j in xrange(C):
            cake[i][j] = row[j]

    for i in xrange(R):
        last = '?'
        for j in xrange(C):
            if cake[i][j] == '?' and last != '?':
                cake[i][j] = last
            elif cake[i][j] != '?':
                last = cake[i][j]

        last = '?'
        for j in xrange(C-1, -1, -1):
            if cake[i][j] == '?' and last != '?':
                cake[i][j] = last
            elif cake[i][j] != '?':
                last = cake[i][j]

    for i in xrange(1, R):
        if cake[i][0] == '?':
            cake[i] = cake[i-1]

    for i in xrange(R-2, -1, -1):
        if cake[i][0] == '?':
            cake[i] = cake[i+1]

    # for i in xrange(R):
    #     for j in xrange(C):
    #         print cake[i][j]
    return cake

for case in xrange(int(input())):
    print 'Case #%d:' % (case+1)
    cake = solve()
    for i in xrange(len(cake)):
        print ''.join(cake[i])
