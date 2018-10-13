import math

def valid_rng(r):
    return r[0] <= r[1]

def intersect(r1, r2):
    if r1[0] > r2[0] or r1[0] == r2[0] and r1[1] > r2[1]:
        r1, r2 = r2, r1
    return r1[1] >= r2[0]

if __name__ == "__main__":
    with open("b.in", "r") as r, open("b.out", "w") as w:
        t = int(r.readline().strip())
        for _ in range(t):
            n, p = map(int, r.readline().strip().split())
            r1 = map(int, r.readline().strip().split())
            q = []
            mi = None
            ma = None
            for i in range(n):
                q.append(map(int, r.readline().strip().split()))
            rng = []
            def rng_cmp(x, y):
                if x[0] < y[0]:
                    return -1
                elif x[0] > y[0]:
                    return 1
                else:
                    return x[1] - y[1]
            for i in range(n):
                rng.append(sorted(map(lambda x: (int(math.ceil(x / 1.1 / r1[i])), int(math.floor(x / .9 / r1[i]))), q[i]), rng_cmp))
            u = [[False] * p] * n
            ans = 0
            for i in range(p):
                if not valid_rng(rng[0][i]):
                    continue
                c = [-1] * n
                c[0] = i
                for j in range(1, n):
                    for k in range(p):
                        if not u[j][k] and valid_rng(rng[j][k]) and intersect(rng[0][i], rng[j][k]):
                            c[j] = k
                            break
                if -1 in c:
                    continue
                for j in range(n):
                    u[j][c[j]] = True
                ans += 1
            w.write("Case #%d: %d\n" % ((_ + 1), ans))
