def Cookie():
    T =  int(raw_input())
    for t in range(1, T+1):
        c, f, x = map(float, raw_input().split())
        rate = 2.0
        time = 0.0
        while x/rate > (c/rate + x/(rate+f)):
            time = time + (c/rate);
            rate = rate + f;
        time =  time + x/rate;
        print "Case #{}: {:.7f}".format(t, time)
Cookie()