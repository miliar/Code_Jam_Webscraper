import sys, itertools, collections
sys.setrecursionlimit(10000)

read_ints = lambda: map(int, raw_input().split())
read_int  = input

for no_t in xrange(1, read_int() + 1):
    n, x = read_ints()
    a = sorted(read_ints())
    u = [False] * n

    ans = n
    for i, item in enumerate(a):
        if not u[i] and (a[i] <= x):
            u[i] = True
            for j in xrange(n - 1, -1, -1):
                if not u[j] and (a[i] + a[j] <= x):
                    u[j] = True
                    ans -= 1
                    break

    print 'Case #%d: %s' % (no_t, ans)
