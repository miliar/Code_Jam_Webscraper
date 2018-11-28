tt = int(raw_input())
for t in xrange(1, tt+1):
    n, k = map(int, raw_input().strip().split())
    level = -1
    kk = k
    while kk > 0:
        level += 1
        kk /= 2
    splits = 2**level
    item = k-splits
    num = (n-splits+1)
    r = num%splits
    q = num/splits + (item < r)
    a = (q-1)/2 + (q%2 == 0)
    b = (q-1)/2
    print 'Case #%d: %d %d' % (t, a, b)
