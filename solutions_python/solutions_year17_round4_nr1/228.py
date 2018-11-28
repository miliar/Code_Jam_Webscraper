T = input()
for cas in xrange(1, T+1):
    N, P = map(int, raw_input().split())
    G = map(int, raw_input().split())

    c = [0 for i in xrange(4)]
    for x in G:
        c[x%P] += 1
    # print c

    ans = c[0]
    if P == 2:
        ans += (c[1]+1)/2
    elif P == 3:
        m = min(c[1], c[2])
        c[1] -= m; c[2] -= m
        ans += m
        ans += (c[1]+2)/3+(c[2]+2)/3
    else:
        m = min(c[1], c[3])
        c[1] -= m; c[3] -= m
        ans += m
        m = c[2]/2
        c[2] -= m
        ans += m
        if c[2] == 0:
            ans += (c[1]+3)/4+(c[3]+3)/4
        else:
            if c[1] >= 2:
                c[1] -= 2
                ans += 1
                ans += (c[1]+3)/4
            elif c[3] >= 2:
                c[3] -= 2
                ans += 1
                ans += (c[3]+3)/4
            else:
                ans += 1
    print "Case #%d: %d" % (cas, ans)

