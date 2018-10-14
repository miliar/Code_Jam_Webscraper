__author__ = 'ml'
import numpy as np


def calccookieRate(F, numFarms):
    return 2 + numFarms * F

def solve(fname):
    data = np.loadtxt(fname,delimiter=' ')
    numCases = int(data[0,0])
    baseIndex = 1
    outFileName = fname + '.results.txt'
    with open(outFileName, "w") as myfile:
            myfile.write("")
    for case in range(0,numCases):
        farmCost = data[baseIndex,0]
        farmRate = data[baseIndex,1]
        goal = data[baseIndex,2]

        numCookies = 0
        t          = 0
        totalTime  = 0
        numFarms   = 0
        cookieRate = calccookieRate(farmRate,numFarms)
        #purchase more farms until it isnt quicker
        while numCookies < goal:

            timeToGoalWithout = (goal - numCookies) / cookieRate

            timeToBuyNextFarm = farmCost / cookieRate
            newRate           = calccookieRate (farmRate,numFarms + 1)

            timeToGoalWith    = (goal - numCookies ) / (newRate)  + timeToBuyNextFarm

            if timeToGoalWith < timeToGoalWithout:
                numFarms += 1
                cookieRate = newRate
                totalTime += timeToBuyNextFarm
            else:
                totalTime = timeToGoalWithout + totalTime
                break
        solution = '{:.7f}'.format(totalTime)
        with open(outFileName, "a") as myfile:
            resultString =  "Case #" + str((case+1)) +": " + solution + '\n'
            myfile.write(resultString)
        baseIndex += 1


def solveCookie():
    files = ['B-large.in','B-small-attempt0.in','cookieTest']
    for file in files:
        solution = solve(file)
        print(file, ' solved!')
    return 0


solveCookie()

