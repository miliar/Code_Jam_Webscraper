test_num = int(raw_input())
for test in xrange(test_num):
    c, f, x = map(float, raw_input().split())
    elapsed, farmed, rate = 0.0, 0.0, 2.0
    while True:
        time1 = x / rate
        time2 = c / rate + x / (rate + f)
        if time1 <= time2:
            elapsed += x / rate
            break
        else:
            elapsed += c / rate
            rate += f
    print 'Case #%d: %0.7f' % (test + 1, elapsed)