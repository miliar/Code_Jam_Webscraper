def time(rate, target):
    return 1.0 * target / rate


def _solve_iter(rate, c, f, x):
    # time if hold steady
    t = time(rate, x)
    w = time(rate, c)

    while True:
        # time if wait to accumulate C, spend
        t2 = w + time(rate + f, x)
        if t < t2:
            return t

        t = t2
        rate += f
        w += time(rate, c)


def solve(c, f, x):
    return _solve_iter(2.0, float(c), float(f), float(x))


def test_ex():
    assert solve(30, 1, 2) == 1
    assert abs(solve(30, 2, 100) - 39.1666667) < 1e-5
    assert abs(solve(30.50000, 3.14159, 1999.19990) - 63.9680013) < 1e-5
    assert abs(solve(500, 4, 2000) - 526.1904762) < 1e-5
    solve(10, 1, 100000)
    solve(100, 1, 100000)


if __name__ == "__main__":

    import sys

    data = open(sys.argv[1] + '.in').readlines()
    outfile = open(sys.argv[1] + '.out', 'w')
    data = data[1:]
    for i, d in enumerate(data, 1):
        c, f, x = map(float, d.strip().split())
        outfile.write("Case #%i: %0.7f\n" % (i, solve(c, f, x)))
