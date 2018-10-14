import sys
sys.setrecursionlimit(10000)

def fung(abec, g, r, c):
    dl = {}
    dr = {}
    db = {}
    du = {}
    for x in abec:
        dl[x] = c
        dr[x] = -1
        du[x] = r
        db[x] = -1
    for i in range(r):
        for j in range(c):
            x = g[i][j]
            dl[x] = min(dl[x],j)
            dr[x] = max(dr[x],j)
            du[x] = min(du[x],i)
            db[x] = max(db[x],i)
    for x in abec:
        zi,zj = du[x], dl[x]
        ki, kj = db[x], dr[x]
        kj += 1
        ki += 1

        i,j = zi, zj
        while i < ki:
            if g[i][j] != g[zi][zj]:
                return False
            j += 1
            if j == kj:
                i += 1
                j = zj
    return True

def rek(abec, g, r, c, i, j):
    if i == r:
        return fung(abec, g, r, c)
    if j == c:
        return rek(abec, g, r, c, i+1, 0)
    if g[i][j] != '?':
        return rek(abec, g, r, c, i,j+1)
    mam = False
    for x in abec:
        g[i][j] = x
        ako = rek(abec, g, r, c, i,j+1)
        if ako:
            mam = True
            break
    if not mam:
        g[i][j] = "?"
    return mam

T = int(input())
for t in range(1, T+1):
    r,c = map(int, input().split())
    g = []
    for i in range(r):
        a = input()
        g.append(list(a))
    print("Case #%d:" % t)
    ab = set()
    for i in range(r):
        for j in range(c):
            if g[i][j] == '?':
                continue
            ab.add(g[i][j])
    abec = list(ab)
    res = rek(abec,g,r,c,0,0)
    for i in range(r):
        print("".join(g[i]))
