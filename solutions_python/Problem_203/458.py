from sys import stdin as IN

for _ in range(int(IN.readline())):
    print "Case #%s:" % (_+1)
    R, C = [int(_) for _ in IN.readline().strip().split()]
    G = [[c for c in IN.readline().strip()] for _ in range(R)]
    l = dict()

    for i in range(R):
        for j in range(C):
            c = G[i][j]
            if c not in l:
                l[c] = []
            l[c].append([i, j])
    if '?' in l:
        del l['?']
    dims = dict()
    for c, ps in l.items():
        ml, mt, Mb, Mr = C, R, -1, -1
        for p in ps:
            mt = min(mt, p[0])
            Mb = max(Mb, p[0])
            ml = min(ml, p[1])
            Mr = max(Mr, p[1])
        dims[c] = [ml, mt, Mb, Mr]
    def check(G, a, b, c):
        for i in a:
            for j in b:
                if G[i][j] not in '?' + c:
                    return
        return True
    CHANGE = True
    while CHANGE:
        CHANGE = False
        for c in dims:
            change = True
            while change:
                change = False
                ml, mt, Mb, Mr = dims[c]
                while ml > 0 and check(G, range(mt, Mb+1), [ml-1],  c):
                    ml -= 1
                    change = True
                while Mr < C-1 and check(G, range(mt, Mb + 1), [Mr + 1], c):
                    Mr += 1
                    change = True
                while mt > 0 and check(G, [mt-1], range(ml, Mr+1), c):
                    mt -= 1
                    change = True
                while Mb < R-1 and check(G,[Mb+1], range(ml, Mr+1), c):
                    Mb += 1
                    change = True
                if change:
                    dims[c] = [ml, mt, Mb, Mr]
                    CHANGE = True
            if CHANGE:
                for c in dims:
                    for i in range(dims[c][1], dims[c][2]+1):
                        for j in range(dims[c][0], dims[c][3]+1):
                            G[i][j] = c
    print "\n".join(["".join(_)for _ in G])
