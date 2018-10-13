INF = 10 ** 19


def show(i, val):
    print "Case #%s: %s" % (i, val)


def sol(d, n, kis, sis):
    if n == 1:
        time = (d - kis[0]) / float(sis[0])
        return d / time

    tmp = sorted([(ki, si) for ki, si in zip(kis, sis)])

    kis = [x[0] for x in tmp]
    sis = [x[1] for x in tmp]

    times = [INF for _ in xrange(n)]
    times[-1] = (d - kis[-1]) / float(sis[-1])
    for i in xrange(n - 2, -1, -1):
        ck, cs = kis[i], sis[i]
        nk, ns = kis[i + 1], sis[i + 1]

        time = (d - kis[i]) / float(sis[i])
        times[i] = max(times[i + 1], time)

    return d / times[0]


if __name__ == "__main__":
    T = int(raw_input().strip())

    for i in xrange(1, T + 1):
        d, n = map(int, raw_input().strip().split())
        kis, sis = [], []
        for _ in xrange(n):
            ki, si = map(int, raw_input().strip().split())
            kis.append(ki)
            sis.append(si)
        show(i, sol(d, n, kis, sis))

