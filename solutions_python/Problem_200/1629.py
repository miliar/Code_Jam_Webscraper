def solve(test):
    a = map(int, str(int(raw_input())))
    n = len(a)
    while True:
        for i in xrange(n - 1):
            if a[i] > a[i + 1]:
                for j in xrange(i + 1, n):
                    a[j] = 9
                for j in xrange(i, -1, -1):
                    a[j] -= 1
                    if a[j] == 0 and j > 0:
                        a[j] -= 1
                    if a[j] < 0:
                        a[j] += 10
                    else:
                        break
                break
        else:
            break
    print 'Case #%s: %s' % (test + 1, int(''.join(map(str, a))))


tests = int(raw_input())
for test in xrange(tests):
    solve(test)
