for _t in range(1, int(raw_input())+1):
    smax, audience = raw_input().strip().split()
    smax = int(smax)
    audience = [int(c) for c in audience]
    cum = [audience[0]] + [0] * smax
    need = 0
    for si in range(1, smax+1):
        if cum[si-1] < si:
            diff = si - cum[si-1]
            need += diff
            cum[si-1] += diff
        cum[si] = audience[si] + cum[si-1]
    print "Case #%d: %d" % (_t, need)
