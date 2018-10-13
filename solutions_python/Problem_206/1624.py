T = input()

for t in xrange(T):
    D, N = map(int, raw_input().split())
    hs = []
    for n in xrange(N):
        pos, speed =  map(int, raw_input().split())
        hs.append([pos, speed])


    hs.sort(key=lambda x: x[0])
    dp, ds = -1, -1
    for i in xrange(1, len(hs)):
        if hs[i-1][1] <= hs[i][1]:
            dp, ds = hs[i-1][0], hs[i-1][1]
            break
        else:
            if (D - hs[i][0]) / float(hs[i][1]) < (hs[i][0] - hs[i-1][0]) / float(hs[i-1][1] - hs[i][1]):
                dp, ds = hs[i-1][0], hs[i-1][1]


    if dp == -1:
        dp, ds = hs[-1][0], hs[-1][1]

    speed = D / ((D-dp)/float(ds))

    print 'Case #%d: %f' % (t+1, speed)

