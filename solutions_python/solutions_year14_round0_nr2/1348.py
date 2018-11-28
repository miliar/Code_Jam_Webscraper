
test_cases = int(raw_input())

for i in xrange(test_cases):
    rate = 2.0
    C, F, X = map(float, raw_input().strip().split())

    d_time = X / rate
    acc_time = 0.0
    while True:
        a = (C / rate) + X / (rate + F)
        if a < d_time:
            # buy it
            acc_time += C / rate
            rate += F
            n_time = acc_time + X / rate
            if d_time > n_time:
                d_time = n_time
            else:
                break
        else:
            break
    print "Case #%d: %0.7f" % (i + 1, d_time)



