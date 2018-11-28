T = int(raw_input())

for c in range(T):
    X, S, R, t, N = map(int, raw_input().split(' '))
    ww = []
    time = 0
    for n in range(N):
        b,e,s = map(int, raw_input().split(' '))
        ww.append((e-b, s))
    ww.append((X-sum([x[0] for x in ww]),0))
    ww.sort(key=lambda x: x[1])

    for (d,s) in ww:
        # Run as much as we can
        if t>0:
            td = d/float(s+R)
            if t >= td:
                t -= td
                time += td
            else:
                time += t
                time += (d-(t*(s+R)))/float(s+S)
                t = 0
        else:
            time += d/float(s+S)

    print "Case #%d: %f" % ((c+1), time)
