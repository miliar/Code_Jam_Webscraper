for tc in xrange(input()):
    dest, nhorses = map(int, raw_input().split())
    horses = [map(int, raw_input().split()) for _ in xrange(nhorses)]
    horses.sort(key=lambda x:x[1])
    ts = []
    for start, speed in horses:
        t = float(dest - start) / speed
        ts.append(t)
    print "Case #%d: %.6f" % (1+tc, float(dest) / max(ts))
