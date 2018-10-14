for case in range(1, input() + 1):
    sm, ss = raw_input().split()
    sm = int(sm)
    xs = [int(i) for i in ss]

    standing = 0
    cnt = 0

    for i in range(len(xs)):
        if standing >= i:
            standing += xs[i]
        else:
            cnt += i - standing
            standing = i + xs[i]

    print "Case #%d: %d" % (case, cnt)
