def solve():
    N, K = map(int, raw_input().strip().split())
    # print N, K

    while K > 1:
        M, m = N//2, (N-1)//2
        if M == m:
            N = m
        else:
            N = m if K % 2 else M
        K //= 2

    return "%d %d" % (N//2, (N-1)//2)

for case in xrange(int(input())):
    print 'Case #%d: %s' % (case+1, solve())
