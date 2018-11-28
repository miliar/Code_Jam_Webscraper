f = open('B-large.in')

numSamples = int(f.readline())

import decimal
from decimal import Decimal as D
# set the precision to double that of float64.. or whatever you want.
decimal.setcontext(decimal.Context(prec=34))


for i in xrange(numSamples):
    line = f.readline().strip()
    args = line.split(' ')
    
    farmCost = D(args[0])
    farmRate = D(args[1])
    goal = D(args[2])

    currentRate = D(2.0)
    myCookies = D(0.0)
    totalTime = D(0.0)
    cdCookies = D(0)

    while True:
        if myCookies >= goal:
            break

        realTime = (goal - myCookies) / currentRate
        farmTime = farmCost / currentRate
        afterFarmTime = (goal - myCookies) / (currentRate + farmRate)

        # You can finish before buying one farm
        if realTime < farmTime:
            myCookies += currentRate * realTime
            totalTime += realTime
            break
        elif realTime < farmTime + afterFarmTime:
            # You can finish faster than buying one farm and waiting for goal
            myCookies += currentRate * realTime
            totalTime += realTime
        else:
            # Buy farm
            totalTime += farmTime
            currentRate += farmRate

    print "Case #{0}: {1}".format(i+1, totalTime)
