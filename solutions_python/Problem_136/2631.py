
absolutePrecision = 1e-5


num_of_tests = int(raw_input())
for test_num in xrange(num_of_tests):
    C, F, X = map(float, raw_input().split())
    cs = 'Case #' + str(test_num) + ':'
    if C >= X:
        print 'Case #%d: %.7f' % (test_num + 1, X / 2)
        continue
    t_passed = 0
    ans = X
    for r in xrange(100001):
        ans = min(ans, t_passed + X / (r * F + 2))
        t_passed += C / (r * F + 2)

    print 'Case #%d: %.7f' % (test_num + 1, ans)



