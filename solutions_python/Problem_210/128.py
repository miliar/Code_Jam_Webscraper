def solve():
    n1, n2 = map(int, raw_input().split())
    l1 = sorted(map(int, raw_input().split()) for _ in xrange(n1))
    l2 = sorted(map(int, raw_input().split()) for _ in xrange(n2))
    if n2 == 2:  # n1 == 0
        n1, n2 = n2, n1
        l1, l2 = l2, l1
    if n1 == 2:
        if l1[1][1] - l1[0][0] > 720:
            if l1[1][0] - l1[0][1] >= 720:
                return 2
            return 4
        return 2
    return 2

T = int(raw_input())
for t in xrange(T):
    print 'Case #%s: %s' % (t+1, solve())
