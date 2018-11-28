test_cases = input()
for test_no in xrange(test_cases):
    N, K = [int(x) for x in raw_input().split()]
    K += 1
    if K%(2**N) == 0:
        print 'Case #' + str(test_no + 1) + ':', 'ON'
    else:
        print 'Case #' + str(test_no + 1) + ':', 'OFF'
