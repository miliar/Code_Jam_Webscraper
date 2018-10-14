def g(x, k):
    t1 = (x - k) / (k + 1)
    n2 = (x - k) % (k + 1)
    n1 = k + 1 - n2 
    t2 = t1 + 1
    if n2 == 0:
        t2 = t1
    return t1, t2, n1, n2

T = int(raw_input())

for i in xrange(T):
    n, k = map(int, raw_input().split())
    if k == 1:
        a, b, c, d = g(n, k)
        print 'Case #' + str(i+1) + ': ' + str(b) + ' ' + str(a)
        continue
    s = 1
    while (s + 1) * 2 - 1 < k:
        s = (s + 1) * 2 - 1
    t1, t2, n1, n2 = g(n, s)
    r = k - s
    if r <= n2:
        a, b, c, d = g(t2, 1)
    else:
        a, b, c, d = g(t1, 1)
    print 'Case #' + str(i+1) + ': ' + str(b) + ' ' + str(a)

        
