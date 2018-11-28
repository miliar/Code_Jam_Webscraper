for cs in xrange(1, input() + 1):
    n = input()
    a = map(int, raw_input().split())
    ans = max(a)
    for i in range(1, ans)[::-1]:
        tmp = i
        for j in a:
            if j > i:
                tmp += (j - i) / i + ((j - i) % i > 0)
        ans = min(ans, tmp)
    print 'Case #%d: %d' % (cs, ans)
