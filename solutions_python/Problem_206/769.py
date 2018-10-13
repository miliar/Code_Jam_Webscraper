def row(fn):
    return map(fn, raw_input().strip().split())

for t in xrange(1, input()+1):
    D, N = row(int)
    horses = sorted([row(float) for _ in xrange(N)])

    ksucc, ssucc = D, 0

    for k, s in reversed(horses):
        tneeded = (D-k) / s

        if k > ksucc: raise RuntimeError()
        if s > ssucc:
            tcoll = (ksucc-k) / (s-ssucc)

            if 0 <= tcoll < tneeded:
                distcoll = s * tcoll
                tneeded = tcoll + (D-k-distcoll) / ssucc

        ksucc, ssucc = k, s

    res = D / tneeded
    print 'Case #%d: %f' % (t, res)
