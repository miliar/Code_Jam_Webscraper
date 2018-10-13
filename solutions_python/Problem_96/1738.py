# Google Code Jam Problem B: Dancing With the Googlers
# Solution by Michael Reinhard

def breakdownStandard(score):
    oneThirdOfScore = score / 3
    if score % 3 == 0:
        return (oneThirdOfScore, oneThirdOfScore, oneThirdOfScore)
    elif score % 3 == 1:
        return (oneThirdOfScore, oneThirdOfScore, oneThirdOfScore + 1)
    elif score % 3 == 2:
        return (oneThirdOfScore, oneThirdOfScore + 1, oneThirdOfScore + 1)

def breakdownSurprising(score):
    oneThirdOfScore = score / 3
    if score < 2 or score > 28:
        return breakdownStandard(score)
    elif score % 3 == 0:
        return (oneThirdOfScore - 1, oneThirdOfScore, oneThirdOfScore + 1)
    elif score % 3 == 1:
        return (oneThirdOfScore - 1, oneThirdOfScore + 1, oneThirdOfScore + 1)
    elif score % 3 == 2:
        return (oneThirdOfScore, oneThirdOfScore, oneThirdOfScore + 2)
 
def bestResultStandard(score):
    return max(breakdownStandard(score))

def bestResultSurprising(score):
    return max(breakdownSurprising(score))


numCases = input()
for case in range(numCases):
    inputList = map(int, raw_input().split())
    numGooglers = inputList[0]
    numSurprising = inputList[1]
    threshold = inputList[2]
    scoreList = inputList[3:]
    scoreList.sort()
    scoreList.reverse()
    numStandardWinners = len(filter(lambda score: 
                                    bestResultStandard(score) >= threshold, 
                                    scoreList))
    standardLosers = filter(lambda score: 
                            bestResultStandard(score) < threshold, scoreList)
    numSurprisingWinners = len(filter(lambda score: 
                                    bestResultSurprising(score) >= threshold, 
                                    standardLosers[:numSurprising]))
    numWinners = numStandardWinners + numSurprisingWinners
    print "Case #" + str(case + 1) + ": " + str(numWinners)
                             
