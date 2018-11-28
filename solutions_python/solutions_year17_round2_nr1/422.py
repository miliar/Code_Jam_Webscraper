for t in range(int(raw_input())):
    d, n = map(int,raw_input().strip().split())
    m = 0
    for __ in range(n):
        k, s = map(int,raw_input().strip().split())
        time = (d-k)/float(s)
        m = max(time, m)

    #print m
    ans = d / float(m)




    print 'Case #{}: {}'.format(t+1, ans)