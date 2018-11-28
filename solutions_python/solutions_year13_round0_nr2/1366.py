fo = open('B-out.txt', 'w')
f = open('B-large.in')
g = []
def isbad(r, c):
    v = g[r][c]
    dng = False
    for i in range(len(g)):
        if not g[i][c] <= v:
            dng = True
            break
    if dng:
        for j in range(len(g[0])):
            if not g[r][j] <= v:
                return True
                break
    return False
for z in range(int(f.readline().strip())):
    r, c = [int(x) for x in f.readline().strip().split()]
    fo.write('Case #%d: ' %(z+1))
    bad = False
    g = []
    for i in range(r):
        g.append([int(x) for x in f.readline().strip().split()])
    for i in range(r):
        for j in range(c):
            bad = isbad(i, j)
            if bad: break
        if bad: break
    if bad: fo.write('NO\n')
    else: fo.write('YES\n')
f.close()
fo.close()
