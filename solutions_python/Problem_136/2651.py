T = int(raw_input())
for t in xrange(T):
    C, F, X = map(float, raw_input().strip().split())
    cps = 2
    last_buy = 0
    total_time = last_buy + X / cps
    new_total_time = total_time

    while(new_total_time <= total_time):
        total_time = new_total_time
        last_buy = last_buy + C / cps
        cps += F
        new_total_time = last_buy + X / cps

    print "Case #%d: %.7f" % (t + 1, total_time)
