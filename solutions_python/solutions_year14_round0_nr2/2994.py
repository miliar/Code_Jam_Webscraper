import sys

__author__ = 'Niels De Bock'

aantalOpgaven = int(raw_input())
for i in range(1,aantalOpgaven+1):
    C,F,X = map(float, raw_input().split())

    best = sys.maxint
    currentCookies, currentTime, currentNbFactories = 0, 0, 0
    while True:
        cookiesPerSecond = 2 + F*currentNbFactories
        extraCookiesNeededForFactory = C - currentCookies
        extraCookiesNeededForWin = X - currentCookies

        #option 1: go for win
        prevBest = best
        best = min(best, currentTime + extraCookiesNeededForWin/cookiesPerSecond)

        #option 2: go for factory:
        currentCookies = 0
        currentTime+=extraCookiesNeededForFactory/cookiesPerSecond
        currentNbFactories+=1

        if prevBest == best:
            break

    print "Case #"+str(i)+": "+str(best)
