CA = input()

def solve(tc):
    N = input()
    m = map(int, raw_input().split())
    a = 0

    for i, x in enumerate(m[1:]):
        if x < m[i]:
            a += m[i] - x

    diff = max(m[i] - x for i, x in enumerate(m[1:]))
    b = 0
    for x in m[:-1]:
        b += min(diff, x)
    return a, b


for tc in range(1, CA + 1):
    a, b = solve(tc)
    print "Case #%d: %d %d" % (tc, a, b)
