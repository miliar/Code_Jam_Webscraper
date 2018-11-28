T = int(raw_input())  

for K in xrange (T):
    d, n = [int(g) for g in raw_input().split(" ")]
    ans = 0
    for i in xrange(n):
        k, s = [int(g) for g in raw_input().split(" ")]
        ans = max(ans, (d - k) * 1.0 / s)
        
    print "Case #{}: {}".format(K+1, d / ans)