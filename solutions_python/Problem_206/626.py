if __name__ == "__main__":
    with open("y.in.in", "r") as r, open("y.out", "w") as w:
        ty = int(r.readline().strip())
        for _ in range(ty):
            d, n = map(int, r.readline().strip().split())
            q = []
            for i in range(n):
                k, s = map(int, r.readline().strip().split())
                q.append((k, s))
            q.sort(cmp=lambda x, y: y[0] - x[0])
            maxv = (d - q[0][0]) / float(q[0][1])
            for i in range(1, len(q)):
                if q[i][1] <= q[i - 1][1] or (q[i - 1][0] - q[i][0]) / float(q[i][1] - q[i - 1][1]) > maxv:
                    maxv = max(maxv, (d - q[i][0]) / float(q[i][1]))
            w.write("Case #%d: %.9lf\n" % ((_ + 1), d / float(maxv)))
