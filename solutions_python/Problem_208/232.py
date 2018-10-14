fin = open("c.in")
fout = open("c.out", "w")

nt = int(fin.readline())

for tn in xrange(nt):
    fout.write("Case #" + str(tn + 1) + ": ")


    n, q = (int(i) for i in fin.readline().split())
    hp = [0] * n
    hs = [0] * n
    INF = 1e20
    ht = [INF] * n

    dist = [0] * n
    for i in range(n):
        hp[i], hs[i] = (int(c) for c in fin.readline().split())
    for i in range(n):
        d = [int(c) for c in fin.readline().split()]
        if i < n - 1:
            dist[i] = d[i + 1]

    ht[0] = 0
    for i in range(1, n):
        # calc time to city i
        for j in range(i):
            hp[j] -= dist[i - 1]
            if hp[j] < 0:
                ht[j] = INF
            else:
                ht[j] += 1. * dist[i - 1] / hs[j]
        ht[i] = min(ht[:i])

    for i in range(q):
        u, k = (int(c) for c in fin.readline().split())
        fout.write(str(ht[-1]))

    fout.write('\n')
    