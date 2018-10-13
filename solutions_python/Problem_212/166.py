import sys, itertools, collections
sys.setrecursionlimit(10000)

read_ints = lambda: map(int, raw_input().split())
read_int  = input


def solve_2(c0, c1):
    ans = c0

    p11 = c1 // 2; ans += p11
    c1 -= p11 * 2

    ans += c1 > 0
    return ans


def solve_3(c0, c1, c2):
    ans = c0

    p12 = min(c1, c2); ans += p12
    c1 -= p12
    c2 -= p12

    p111 = c1 // 3; ans += p111
    c1 -= p111 * 3

    p222 = c2 // 3; ans += p222
    c2 -= p222 * 3

    ans += max(c1, c2) > 0
    return ans


def solve_4(c0, c1, c2, c3):
    ans = c0

    p13 = min(c1, c3); ans += p13
    c1 -= p13
    c3 -= p13

    p22 = c2 // 2; ans += p22
    c2 -= p22 * 2

    p112 = min(c1 // 2, c2); ans += p112
    c1 -= p112 * 2
    c2 -= p112

    p233 = min(c2, c3 // 2); ans += p233
    c2 -= p233
    c3 -= p233 * 2

    p1111 = c1 // 4; ans += p1111
    c1 -= p1111 * 4

    p3333 = c3 // 4; ans += p3333
    c3 -= p3333 * 4

    ans += max(c1, c2, c3) > 0
    return ans


for no_t in xrange(1, read_int() + 1):
    n, p = read_ints()
    c = collections.Counter([x % p for x in read_ints()])

    if p == 2:
        ans = solve_2(c[0], c[1])
    elif p == 3:
        ans = solve_3(c[0], c[1], c[2])
    elif p == 4:
        ans = solve_4(c[0], c[1], c[2], c[3])

    print 'Case #%d: %s' % (no_t, ans)
