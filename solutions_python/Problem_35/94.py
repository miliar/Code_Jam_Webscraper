N = int(raw_input())

dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]

a, b, c  = [], [], []
for i in xrange(100):
    a.append([0]*100)
    b.append([0]*100)
    c.append([0]*100)

for K in xrange(N):
    ch = 0
    arr = raw_input().split()
    h, w = int(arr[0]), int(arr[1])
    for i in xrange(h):
        arr = raw_input().split()
        for j in xrange(w):
            a[i][j] = int(arr[j])
        
    Sx, Sy = [], [] # stacks for coordinates of cells
    for i in xrange(h):
        for j in xrange(w):
            m, n = 10000, -1
            for k in xrange(4):
                x, y = i + dx[k], j + dy[k]
                if x >= 0 and x < h and y >= 0 and y < w and a[x][y] < m:
                    m, n = a[x][y], k

            if m < a[i][j]:
                b[i][j] = n;
            else:
                b[i][j], c[i][j] = -1, ch
                ch = ch + 1
                Sx.append(i)
                Sy.append(j)

    while len(Sx) > 0:
        i, j  = Sx.pop(), Sy.pop()
        for k in xrange(4):
                x, y = i + dx[k], j + dy[k]
                if x >= 0 and x < h and y >= 0 and y < w and b[x][y] + k == 3:
                    b[x][y] = -1
                    Sx.append(x)
                    Sy.append(y)
                    c[x][y] = c[i][j]

    mp, ch = ['.']*26, 'a'
    for i in xrange(h):
        for j in xrange(w):
            if mp[c[i][j]] == '.':
                mp[c[i][j]] = ch
                ch = chr(ord(ch) + 1)

    print "Case #%d:" % (K+1)
    for i in xrange(h):
        str = ''
        for j in xrange(w):
            str += mp[c[i][j]] + ' '
        print str