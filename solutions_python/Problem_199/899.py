import sys, itertools, collections
sys.setrecursionlimit(10000)

read_ints = lambda: map(int, raw_input().split())
read_int  = input


def gao(s, k):
    a = [c == '+' for c in s]
    n = len(s)
    ans = 0
    for i in xrange(n - k + 1):
        if not a[i]:
            for j in xrange(k):
                a[i + j] = not a[i + j]
            ans += 1

    return ans if all(a) else 'IMPOSSIBLE'


for no_t in xrange(1, read_int() + 1):
    s, k = raw_input().split()
    print 'Case #%d: %s' % (no_t, gao(s, int(k)))
