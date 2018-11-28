import sys, itertools, collections
sys.setrecursionlimit(10000)

read_ints = lambda: map(int, raw_input().split())
read_int  = input


def is_tidy(s):
    for c, d in zip(s, s[1:]):
        if c > d:
            return False
    return True


for no_t in xrange(1, read_int() + 1):
    s = raw_input()
    n = len(s)

    if is_tidy(s):
        ans = int(s)
    else:
        ans = 0

    for i in xrange(1, n):
        base = 10 ** (n - i)
        t = int(s[:i]) * base - 1
        if is_tidy(str(t)):
            ans = max(ans, t)

    print 'Case #%d: %s' % (no_t, ans)
