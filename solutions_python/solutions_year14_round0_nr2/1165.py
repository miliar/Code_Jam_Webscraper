from sys import stdin

T = int(stdin.readline())

for i in xrange(1, T+1):
    C, F, X = map(float, stdin.readline().split())
    #C - farm cost
    #F - farm cookie/sec
    #X - goal
    sec = 0.0
    rate = 2.0
    cookies = 0.0
    while cookies < X:
        sec_without_farms = (X - cookies)/rate
        sec_with_farm = (C - cookies)/rate + X/(rate + F)
        #print 'Sec:{0}, Rate:{1}, Cookies={2}'.format(sec, rate, cookies)
        #print sec_with_farm, sec_without_farms
        if sec_without_farms <= sec_with_farm:
            sec += sec_without_farms
            cookies = X
        else:
            sec += (C - cookies)/rate
            rate += F
            cookies = 0.0

    print 'Case #{0}: {1}'.format(i, sec)
    #break




