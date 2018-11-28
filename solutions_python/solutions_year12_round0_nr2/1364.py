import sys

def solve_case(n, s, p, points):
    m = 0
    for k in points:
        if 3 * p <= k + 2:
            m += 1
        elif 3 * p <= k + 4 and s > 0 and k >= p:
            m += 1
            s -= 1
    return m

def main():
    f = sys.stdin
    t = int(f.readline().strip())
    for i in xrange(t):
        line = f.readline().strip()
        vars = line.split(' ')
        n = int(vars[0])
        s = int(vars[1])
        p = int(vars[2])
        points = map(lambda x:int(x), vars[3:])
        answer = solve_case(n, s, p, points)
        print 'Case #%d: %d' % (i + 1, answer)


if __name__ == '__main__':
    main()