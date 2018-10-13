'''

CurrentAmount + rate*timeLeft = X
timeLeft = (X - CurrentAmount) / rate
timeTillFarm = (C - CurrentAmount) / rate


def findRemainingTime(CurrentAmount, rate, X, C, F):
    timeLeft = (X - CurrentAmount) / rate
    timeToBuyFarm = (C - CurrentAmount) / rate
    if timeLeft < timeToBuyFarm + (X - CurrentAmount)/(rate + F):
        #if the time left without buying a farm is less than the time left without buying a farm, don't buy any more farms.
        return timeLeft
    else:
        #Otherwise return the amount of time to buy a farm plus the amount of time left after buying the farm.
        return timeToBuyFarm + findRemainingTime(CurrentAmount, rate + F, X, C, F)
'''

def findRemainingTime(rate, X, C, F):
    totalTime = 0
    while(1):
        timeToBuyFarm = C / rate
        if X/rate < timeToBuyFarm + X/(rate + F):
            totalTime += X/rate
            return totalTime
        else:
            totalTime += C / rate #Increase the time remaining by the time to buy a farm.
            rate += F


inFile = open("B-large.in", "r")
outFile = open("output.txt", "w")

numTests = int(inFile.readline())

for i in range (numTests):
    values = (inFile.readline().rstrip()).split(" ")
    C = float(values[0])
    F = float(values[1])
    X = float(values[2])
    result = findRemainingTime(2, X, C, F)
    outFile.write("Case #{}: {}\n".format(i+1, result))
