def f(l, k):
    return k + sum([(x-1)/k for x in l])

T = int(raw_input())
for t in xrange(T):
    D = int(raw_input())
    l = map(int, raw_input().split())
    ans = min([f(l, k) for k in xrange(1, 1001)])
    print "Case #{}: {}".format(t+1, ans)
            
