T = int(raw_input())
for t in range(1, T+1):
    ans = 0
    s_max, s = str(raw_input()).lstrip().rstrip().split(' ')
    s_max = int(s_max)
    si = {}
    for i in range(s_max + 1):
        si.update( { i : int(s[i]) } )
    ova = si[0]
    for i in range(1, s_max + 1):
        for j in range(si[i]):
            if i - ova > 0:
                ans += i - ova
                ova += ans
            ova += 1

    print 'Case #%d: %d' % (t, ans)
