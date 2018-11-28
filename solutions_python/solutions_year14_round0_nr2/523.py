T = input()
for t in range(1, T + 1):
    C, F, X = map(float, raw_input().split())
    ret = 0.0
    current_rate = 2.0
    while 1:
        ret += C / current_rate
        if ((X - C) / current_rate) > X / (current_rate+F):
            current_rate += F
        else:
            ret += (X - C) / current_rate
            break
    print "Case #%d: %.7f" % (t, ret)