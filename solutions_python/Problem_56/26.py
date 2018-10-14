
filename = 'A-large'

DIR = [[1, 0], [0, 1], [1, 1], [1, -1]]

fin = open(filename + '.in')
fout = open(filename + '.out', 'w')
cases = int(fin.readline().strip())
for case in xrange(1, cases + 1):
    n, k = [int(x) for x in fin.readline().strip().split()]
    grid = []
    for i in xrange(n):
        grid.append(fin.readline().strip())
    ngrid = []
    ggrid = []
    for i in xrange(n):
        ngrid.append([])
        ggrid.append([])
        for j in xrange(n):
            ngrid[i].append(grid[n - j - 1][i])
            ggrid[i].append('.')
    for j in xrange(n):
        p = n
        for i in xrange(n - 1, -1, -1):
            if ngrid[i][j] != '.':
                p -= 1
                ggrid[p][j] = ngrid[i][j]
    fr = False
    fb = False
    for i in xrange(n):
        for j in xrange(n):
            for d in xrange(4):
                x = i
                y = j
                ffr = True
                ffb = True
                for p in xrange(k):
                    if 0 <= x < n and 0 <=y < n:
                        if ggrid[x][y] != 'B': ffb = False
                        if ggrid[x][y] != 'R': ffr = False
                    else:
                        ffb = ffr = False
                        break
                    x += DIR[d][0]
                    y += DIR[d][1]
                if ffr:
                    fr = True
                if ffb:
                    fb = True
                    #print i, j, x, y, d
    if fr and fb:
        ans = 'Both'
    elif fr and not fb:
        ans = 'Red'
    elif not fr and fb:
        ans = 'Blue'
    else:
        ans = 'Neither'
    print ans
    fout.write('Case #%d: %s\n' % (case, ans))
fin.close()
fout.close()
