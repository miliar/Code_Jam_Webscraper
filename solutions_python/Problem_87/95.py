T = int(raw_input())
for tid in xrange(T):
    (X, S, R, t, N) = [float(x) for x in raw_input().split(' ')]
    wmap = {}
    wmap[0] = X
    for n in xrange(int(N)):
        tokens = raw_input().split(' ')
        di = float(tokens[1]) - float(tokens[0])
        wi = float(tokens[2])
        wmap[0] -= di
        wmap[wi] = wmap.get(wi, 0.0) + di
    answer = 0.0
    for wi in sorted(wmap.iterkeys()):
        di = wmap[wi]
        if t > 0:
            ti = di / (wi + R)
            if ti <= t:
                t -= ti
                answer += ti
            else:
                drest = di - t * (wi + R)
                answer += t + drest / (wi + S)
                t = 0
        else:
            answer += di / (wi + S)
    print "Case #%d: %f" % ((tid + 1), answer)

