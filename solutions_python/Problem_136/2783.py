def readInput():
    out = "Case #{}: {:.7f}"
    caseCount = int(input())
    for caseNum in range(1, caseCount + 1):
        farmCost, increment, target = [float(num) for num in input().split()]
        time = calcMinWait(farmCost, increment, target)
        print(out.format(caseNum, time))

def calcMinWait(farmCost, increment, target):
    farmRate = 2.0
    waited = 0.0
    waitTime = calcWaitTime(farmRate, target)
    buyTime = calcBuyTime(farmRate, farmCost)
    buyWaitTime = buyTime + calcWaitTime(farmRate + increment, target)
    while buyWaitTime < waitTime:
        waited += buyTime
        farmRate += increment
        waitTime = calcWaitTime(farmRate, target)
        buyTime = calcBuyTime(farmRate, farmCost)
        buyWaitTime = buyTime + calcWaitTime(farmRate + increment, target)
    waited += waitTime
    return waited

def calcWaitTime(farmRate, target):
    return target / farmRate

def calcBuyTime(farmRate, farmCost):
    return farmCost / farmRate

if __name__ == "__main__":
    readInput()