T = int(raw_input())

for i in range(T):
    A = [int(x) for x in raw_input().split()]
    N, S, p = A[:3]
    A = A[3:]
    ans = 0
    for t in A:
        x = t
#        print x/3,
        x -= x / 3
#        print x/2,
        x -= x / 2
#        print x
        if x >= p:
            ans += 1
        if x and x==p-1 and S and t%3!=1 :
            S -= 1
            ans += 1
    print 'Case #%d: %d' % (i+1, ans)
