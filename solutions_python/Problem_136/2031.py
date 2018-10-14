

def worthIt(cost, curRate, boost, goal):
    # calculate whether we will finish earlier if buy
    timeToFinish = goal / curRate

    timeToBoost = cost / curRate
    timeFromBoost = goal / (curRate + boost)

    if timeToFinish < timeToBoost + timeFromBoost:
        return False
    else:
        return True

T = input()
for test in xrange(T):
    [C, F, X] = [float(x) for x in raw_input().split(' ')]

    curTime = 0
    curRate = 2.0
    while worthIt(C, curRate, F, X):
        curTime += C / curRate
        curRate += F
    answer = (X / curRate) + curTime

    print 'Case #' + str(test + 1) + ': ' + "{:1.7f}".format(answer)

