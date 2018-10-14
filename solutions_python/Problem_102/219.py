from sys import stdin

eps = 0.000001

class ContPoints:
    index = 0
    val = 0


def solve():
    T = int(stdin.readline())
    for casenum in range(T):
        rs = solve_case()
        print 'Case #%d: %s' % (casenum + 1, rs)


def solve_case():
    # read input
    inp = [int(x) for x in stdin.readline().split()]
    n = inp[0]
    points = []
    i = 0
    for s in inp[1:]:
        p = ContPoints()
        p.index = i
        p.val = s
        points.append(p)
        i += 1
    x = sum(inp[1:])
    # solve
    results = [0] * n
    points.sort(key=lambda p: p.val)

    i = 0
    for p in points:
        j = i if i != 0 else 1
        while True:
            m = j + 1 if j < n else n-1
            dsum = sum(p.val - points[k].val for k in range(m))
            y = 1.0 * (x - dsum) / x / (j + 1)
            if (y < 0):
                results[p.index] = 0
                break
            if (j == n-1) or ((p.val + y*x - points[j+1].val <= 0)
                and (p.val + y*x - points[j].val >= 0)):
                results[p.index] = y
                break
            j += 1
        i += 1
    
    return ' '.join('{0:.6f}'.format(results[i] * 100) for i in range(n))


if __name__ == '__main__':
    solve()
