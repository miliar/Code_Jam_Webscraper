import math

fin = open('C-small-attempt1.in', 'r')
fout = open('C-small-attempt1.out', 'w')

t = int(fin.readline())
for i in xrange(1, t + 1):
    n, q = [int(ssss) for ssss in fin.readline().strip().split(" ")]
    e = [0] * n
    s = [0] * n
    for j in range(n):
        e[j], s[j] = [int(ssss) for ssss in fin.readline().strip().split(" ")]
    d = [[0] * n] * n
    for j in range(n):
        d[j] = [int(ssss) for ssss in fin.readline().strip().split(" ")]
    u, v = [int(ssss) for ssss in fin.readline().strip().split(" ")]
    u -= 1
    v -= 1

    ans = [0] * n
    for j in range(n):
        ans[j] = [100000000000] * n
    eee = [0] * n
    for j in range(n):
        eee[j] = [0] * n
    ans[u] = [0] * n
    while u != v:
        for k in range(n):
            if eee[u][k] >= d[u][u + 1]:
                eee[u + 1][k] = eee[u][k] - d[u][u + 1]
                ans[u + 1][k] = ans[u][k] + d[u][u + 1] * 1.0 / s[k]
        if e[u] >= d[u][u + 1]:
            eee[u + 1][u] = e[u] - d[u][u + 1]
            ans[u + 1][u] = min(ans[u]) + d[u][u + 1] * 1.0 / s[u]
        u = u + 1

    print>>fout, "Case #{}: {}".format(i, min(ans[v]))

fin.close()
fout.close()
