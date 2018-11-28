tests = int(input())
for tt in range(1, tests + 1):
    n, q = [int(s) for s in input().split(" ")]
    
    hd = []
    hs = []
    for i in range(n):
        hd1, hs1 = [int(s) for s in input().split(" ")]
        hd.append(hd1)
        hs.append(hs1)
    
    d = []
    for i in range(n):
        d.append([float(s) for s in input().split(" ")])
        for j in range(n):
            if d[i][j] == -1:
                d[i][j] = 1e100

    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    b = [[1e100 for k in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if d[i][j] <= hd[i]:
                b[i][j] = d[i][j] / hs[i]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                b[i][j] = min(b[i][j], b[i][k] + b[k][j])

    res = []
    for qq in range(q):
        s, t = [int(s) for s in input().split(" ")]
        res.append(str(b[s - 1][t - 1]))

    s = " ".join(res)
    print("Case #{}: ".format(tt) + s)
