#!/usr/bin/python

if __name__ == "__main__":
    cases = int(raw_input())
    currentCase = 1
    results = []
    while currentCase <= cases:
        rate = 2.0
        time = 0.0
        temptime = 0.0
        cookies = 0.0
        C, F, X = raw_input().split(' ')
        C = float(C)
        F = float(F)
        X = float(X)
        while cookies != X:
            temptime = (X - cookies) / rate
            timeToBuyNextFarm = (C - cookies) / rate
            temprate = rate + F
            temptimeAfterFarm = X / temprate
            if (timeToBuyNextFarm + temptimeAfterFarm) <= temptime:
                rate = temprate
                cookies = 0
                time = time + timeToBuyNextFarm
            else:
                time = time + temptime
                cookies = X
        results.append((currentCase, time))
        currentCase += 1
    for i in range(0, cases):
        print "Case #" + str(results[i][0]) + ": " + str(results[i][1])
