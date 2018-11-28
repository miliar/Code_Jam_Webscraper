for t in range(int(raw_input())):
    args = map(int, raw_input().split(' '))
    _,S,p = args[:3]
    scores = args[3:]
    n = 0

    for score in scores:
        div, mod = divmod(score, 3)
        best = div + (mod and 1)
        if best >= p:
            n += 1
        elif S and score and best == p - 1:
            S -= 1
            n += 1

    print "Case #%d: %d" % (t+1, n)
