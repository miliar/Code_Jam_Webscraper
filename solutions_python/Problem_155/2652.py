def read_input():
    n, p = raw_input().split(' ')
    n = int(n)
    p = map(int, p)
    return (n, p)


def solve_problem(inp):
    n, p = inp
    res, tot = 0, 0
    for i in xrange(n+1):
        res = max(res, i - tot)
        tot = tot + p[i]

    return res


def print_output(t, output):
    print 'Case #%i: %i' % (t, output)


if __name__ == "__main__":
    t = int(raw_input())
    for i in xrange(t):
        print_output(i + 1, solve_problem(read_input()))

