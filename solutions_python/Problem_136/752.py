import sys
line = sys.stdin.readline()
numTests = int(line)
for test in xrange(1, numTests+1):
    params = sys.stdin.readline().split(' ')
    C = float(params[0])
    F = float(params[1])
    X = float(params[2])

    cookies = 0.0
    time = 0.0
    R = 2
    while(1):
        timeToX = (X - cookies)/R
        timeToC = C/R
        if (timeToC < timeToX):
            # Reach time where you can buy
            time += timeToC
            cookies += C
            timeToXwithBuy = (X + C - cookies)/(R + F)
            timeToXwithOutBuy = (X - cookies)/(R)
            if (timeToXwithBuy < timeToXwithOutBuy):
                R += F
                cookies -= C
            else:
                time += timeToXwithOutBuy
                break
        else:
            time += timeToX
            break
    print 'Case #%d: %.7f' %(test, time)        
