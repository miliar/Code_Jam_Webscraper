if __name__ == "__main__":
    with open("c.in", "r") as r, open("c.out", "w") as w:
        t = int(r.readline().strip())
        for _ in range(1, t + 1):
            n, q = map(int, r.readline().strip().split())
            e = []
            s = []
            for i in range(n):
                x, y = map(int, r.readline().strip().split())
                e.append(x)
                s.append(y)
            d = [0]
            for i in range(n):
                x = map(int, r.readline().strip().split())
                if i < n - 1:
                    d.append(x[i + 1])
            for i in range(1, n):
                d[i] += d[i - 1]
            for i in range(q):
                r.readline()
            f = [0]
            for i in range(1, n):
                t = None
                for j in range(i - 1, -1, -1):
                    if d[i] - d[j] > e[j]:
                        continue
                    t2 = f[j] + (d[i] - d[j]) / float(s[j])
                    if t == None or t2 < t:
                        t = t2
                f.append(t)
            w.write("Case #%d: %.9lf\n" % (_, f[n - 1]))
