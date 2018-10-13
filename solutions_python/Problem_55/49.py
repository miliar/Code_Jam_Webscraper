from sys import stdin

def riadok():
    return map(int, stdin.readline().split())

for cas in range(int(stdin.readline())):
    (r, k, n) = riadok()
    g = riadok()
    su = sum(g)
    if su <= k: res = r * su
    else:
        f, e = [0] * n, [0] * n
        for i in range(n):
            su, j = 0, i
            while su + g[j] <= k:
                su += g[j]
                j = (j + 1) % n
            f[i], e[i] = j, su

        kedy = [-1] * n
        cnt, act = 0, 0
        while kedy[act] == -1:
            kedy[act] = cnt
            act, cnt = f[act], cnt + 1
        pr, dl = kedy[act], cnt - kedy[act]

        res, act = 0, 0
        for i in range(0, min(pr, r)):
            res += e[act]
            act = f[act]

        if r > pr:
            r -= pr
            round = 0
            for i in range(dl):
                round += e[act]
                act = f[act]
            res += round * (r / dl)
            r %= dl
            for i in range(r):
                res += e[act]
                act = f[act]

    print "Case #%d: %d" % (cas + 1, res)
