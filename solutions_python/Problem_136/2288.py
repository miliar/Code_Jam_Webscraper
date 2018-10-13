def cookie():
    for t in xrange(input()):
        c,f,x = map(float,raw_input().split())
        gain = 0.0
        total = 0.0
        rate = 2.0
        while True:
            if (total + c/rate + x/(rate+f)) < (total + x/rate):
                total = total + c/rate
                rate = rate + f
                #print total
            else:
                total = total + x/rate
                break
        print 'Case #%d: %.7f' %((t+1),round(total,7))
cookie()
