#!/usr/bin/env python

def getCookieTime(C, F, X, RATE, FARM_COUNT):
    time = 0.0
    currentRate = RATE
    for x in range(0, FARM_COUNT):
        time += (C / currentRate)
        currentRate += F
    
    time += X / currentRate

    return time

T = int(raw_input())
for i in range(T):
    params = list(float(s) for s in raw_input().split(' '))

    RATE = 2.0

    C = params[0] # cookie cost per farm
    F = params[1] # cookies earned per farm
    X = params[2] # target cookie balance

    bestResults = float("inf")

    # Determine a best guess number for the number of farms to buy that is too large
    # Adjust the best guess with a fudge factor
    bestGuess = int((X / C) + 0.5) + 10
    farmCount = bestGuess

    while True:
        time = getCookieTime(C, F, X, RATE, farmCount)
        farmCount = farmCount - 1

        if (time < bestResults):
            bestResults = time
        else:
            print 'Case #{0:d}: {1:0.7f}'.format(i+1, bestResults)
            break
