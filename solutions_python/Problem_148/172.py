t = int(raw_input())
for iCase in range(1,t+1):
    n,x = map(int,raw_input().split())
    v = map(int,raw_input().split())
    v.sort()
    c = 0
    i,j = 0,n-1
    while i <= j:
        if i < j and v[i]+v[j] <= x:
            i += 1
            j -= 1
        else:
            j -= 1
        c += 1
    print 'Case #%d: %d' % (iCase, c)