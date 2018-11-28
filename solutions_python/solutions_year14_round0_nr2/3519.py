t = int(raw_input())
for i in xrange(t):
    c, f, x = map(float, raw_input().split())
    tmp = -1
    time_spent = 0.0
    curr_rate = 2.0
    while True:
        tot_time_not_buy = time_spent + x / curr_rate 
        tot_time_buy = time_spent + c / curr_rate + x / (curr_rate + f)
        if tot_time_buy < tot_time_not_buy:
            time_spent += c / curr_rate
            curr_rate += f
        else:
            time_spent += x/curr_rate
            break
    print "Case #%s: %s" % (i+1, time_spent)
