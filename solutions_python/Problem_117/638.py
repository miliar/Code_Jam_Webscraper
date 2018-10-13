def cut(k,n,m):
    global a
    row = []
    col = []
    for i in xrange(n):
        count = 0
        for j in xrange(m):
            if a[i][j] == k :
                count += 1
        if count == m:
            row.append(i)
    for i in xrange(m):
        count = 0
        for j in xrange(n):
            if a[j][i] == k :
                count += 1
        if count == n:
            col.append(i)

    for i in xrange(n):
        for j in xrange(m):
            if i in row or j in col :
                a[i][j] += 1


def end(a):
    key = a[0][0]
    for i in xrange(n):
        for j in xrange(m):
            if a[i][j] != key :
                return False
    return True


t = int(raw_input())
for ab in xrange(t):
    x = map(int,raw_input().split())
    n = x[0]
    m = x[1]
    a = []
    for i in xrange(n):
        a.append(map(int,raw_input().split()))
    i = 1
    while True:
        cut(i,n,m)
        i += 1
        if i > 2:
            flag = 0
            break
        if end(a) :
            flag = 1
            break
    print "Case #%d:" %(ab+1),
    if flag :
        print "YES"
    else :
        print "NO"
