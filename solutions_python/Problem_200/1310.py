def calc(n):
    if n < 10:
        return n
    ans = calc(n / 10)
    if ans % 10 <= n % 10:
        return ans * 10 + n % 10
    elif ans < n / 10:
        return ans * 10 + 9
    else:
        return calc(ans - 1) * 10 + 9

T = input()
for test in xrange(T):
    n = input()
    ans = calc(n)
    print 'Case #%d: %d' % (test + 1, ans)
