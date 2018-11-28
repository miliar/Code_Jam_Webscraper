def calc(n, k):
    if n == k:
        return (0, 0)
    if k == 1:
        return (n/2, (n-1)/2)
    if k % 2 == 0:
        return calc(n/2, k/2)
    else:
        return calc((n-1)/2, (k-1)/2)

t = int(raw_input())
for case in xrange(1, t+1):
    print "Case #"+str(case)+":",
    N, K = map(int, raw_input().split())
    l, r = calc(N, K)
    print str(l), str(r)

