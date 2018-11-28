def row_fill_util(g, x, y, m, n, val):
    if y<n-1 and g[x][y+1] == '?':
        g[x][y+1] = val
        row_fill_util(g, x,y+1, m, n, val)

    if y>0 and g[x][y-1] == '?':
        g[x][y-1] = val
        row_fill_util(g, x,y-1, m, n, val)


def col_fill_util(g, x, y, m, n, val):
    if x<m-1 and g[x+1][y] == '?':
        g[x+1][y] = val
        col_fill_util(g, x+1,y, m, n, val)

    if x>0 and g[x-1][y] == '?':
        g[x-1][y] = val
        col_fill_util(g, x-1,y, m, n, val)



def row_fill(g, x, y, m, n):
    val = g[x][y]
    if val == '?':
        return
    row_fill_util(g, x, y, m, n, val)

def col_fill(g, x, y, m, n):
    val = g[x][y]
    if val == '?':
        return
    col_fill_util(g, x, y, m, n, val)




for t in range(int(raw_input())):
    r, c = map(int,raw_input().strip().split())
    g = []
    for i in range(r):
        g.append(list(raw_input()))

    #print g

    for i in range(r):
        for j in range(c):
            row_fill(g, i, j, r, c)

    for i in range(r):
        for j in range(c):
            col_fill(g, i, j, r, c)



    print 'Case #{}:'.format(t+1)

    for i in g:
        print ''.join(str(j) for j in i)

