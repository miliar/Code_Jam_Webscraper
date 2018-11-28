t = input()
for cas in xrange(t):
    s, k = raw_input().split()
    a = [1 if ch == '+' else 0 for ch in s]
    k = int(k)

    res = 0
    n = len(a)
    for i in xrange(n-k+1):
        if a[i] == 0:
            res += 1
            for j in xrange(i, i+k):
                a[j] = 1-a[j]

    if sum(a) == n:
        print 'Case #{0}: {1}'.format(cas+1, res)
    else:
        print 'Case #{0}: IMPOSSIBLE'.format(cas+1)
