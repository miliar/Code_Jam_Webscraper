def paint(cake, w, i, j):
    for c in range(0, j)[::-1]:
        if cake[i][c] == '?':
            cake[i][c] = w
        else:
            break
    for c in range(j+1, len(cake[0])):
        if cake[i][c] == '?':
            cake[i][c] = w
        else:
            break
    return
    

def alphabet_cake():
    R, C = map(int, raw_input().strip().split())
    cake = []
    lookup = {}
    for i in xrange(R):
        cake.append(list(raw_input().strip()))
        for j in xrange(C):
            if cake[i][j] != '?':
                if cake[i][j]  not in lookup:
                    lookup[cake[i][j]] = (i, j)
    for w, p in lookup.iteritems():
        paint(cake, w, *p)
    for i in xrange(1, R):
        if cake[i][0] == '?' and cake[i-1][0] != '?':
            cake[i] = cake[i-1]
    for i in reversed(xrange(0, R-1)):
        if cake[i][0] == '?' and cake[i+1][0] != '?':
            cake[i] = cake[i+1]
    for i in xrange(R):
        print "".join(cake[i])
    

for case in xrange(input()):
    print 'Case #%d:' % (case+1)
    alphabet_cake()
