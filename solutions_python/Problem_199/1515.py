def solve():
    s, k = raw_input().split()
    n, k = len(s), int(k)
    s = [1 if c == '-' else 0 for c in s]
    res = 0
    for i in xrange(n - k + 1):
        if s[i]:
            for j in xrange(i, i + k):
                s[j] = 1 - s[j]
            res += 1
    return res if sum(s) == 0 else None


tests = int(raw_input())
for test in xrange(tests):
    result = solve()
    print 'Case #%s: %s' % (
        test + 1, 'IMPOSSIBLE' if result is None else result)
