def solve(row, col, li):
    r = []
    for i in xrange(row):
        r.append(['x'] * col)
    for i in xrange(row):
        for j in xrange(col):
            if li[i][j] == '.':
                #print "rep:{0}:{1}".format(i,j)
                r[i][j] = '.'
        #print "@@{0}".format(li[i])
        #print "$${0}".format(r[i])
    for i in xrange(row):
        if i + 1 == row:
            break
        for j in xrange(col):
            if j + 1 == col:
                break
            if r[i][j] == 'x' and r[i][j+1] == 'x':
                if r[i+1][j] == 'x' and r[i+1][j+1] == 'x':
                    r[i  ][j  ] = '/'
                    r[i  ][j+1] = '\\'
                    r[i+1][j  ] = '\\'
                    r[i+1][j+1] = '/'
    for i in xrange(row):
        if 'x' in r[i]:
            return []
    return r

t = int(raw_input())
for i in xrange(t):
    row, col = map(int, raw_input().split())
    li = []
    for j in xrange(row):
        line = raw_input()
        li.append(line)
        #print "$${0}".format(line)

    r = solve(row, col, li)
    print "Case #{0}:".format(i + 1)
    if len(r) == 0:
        print "{0}".format("Impossible")
    else:
        for j in xrange(row):
            print "{0}".format(''.join(r[j]))
