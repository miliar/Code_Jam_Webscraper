test_case = input()
for _ in xrange(1, test_case + 1):
    d, n = map(int, raw_input().split())
    ans = 0.
    for i in xrange(n):
        k, s = map(int, raw_input().split())
        t = float(d - k) / s
        #print t
        ans = max(ans, t)
    print 'Case #' + str(_) + ': ' + str(d / ans)
