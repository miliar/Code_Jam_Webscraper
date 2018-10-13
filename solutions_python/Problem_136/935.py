for i in xrange(input()):
    C, F, X = map(float, raw_input().split())
    time = 0
    rate = 2
    while (X / rate) > (X / (rate + F)) + (C / rate):
        time += C / rate
        rate = rate + F

    time += X / rate
    print "Case #%d: %.7f" % (i + 1, time)
