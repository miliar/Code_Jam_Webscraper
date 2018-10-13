__author__ = 'archeg'

class solveB():

    def __init__(self, farmCost, farmBenefit, winReq):
        self.farmCost = farmCost
        self.farmBenefit = farmBenefit
        self.winReq = winReq
        self.numberOfFarms = 0
        self.currentSeconds = 0
        self.currentCookies = 0

    def secondsToTargetIfNoBuy(self, targetCookies):
        return (targetCookies - self.currentCookies) / (self.numberOfFarms * self.farmBenefit + 2.)

    def secondsToHaveMoreCookiesIfBuy(self):
        return self.farmCost / self.farmBenefit

    def buyFarm(self):
        self.numberOfFarms += 1
        self.currentCookies -= self.farmCost

    def advance(self):
        self.currentSeconds += self.secondsToTargetIfNoBuy(self.farmCost)
        self.currentCookies = self.farmCost

    def compute(self):
        while True:
            self.advance()
            secondsToWin = self.secondsToTargetIfNoBuy(self.winReq)
            secondsToHaveMoreCookiesIfBuy = self.secondsToHaveMoreCookiesIfBuy()

            #print "[%f %f %f]" % (self.currentSeconds, self.currentCookies, self.numberOfFarms)
            #print "(%f %f)" % (secondsToWin, secondsToHaveMoreCookiesIfBuy)
            if (secondsToWin > secondsToHaveMoreCookiesIfBuy):
                self.advance()
                self.buyFarm()
            else:
                print secondsToWin
                return self.currentSeconds + secondsToWin


def Run(fileName, runOnly = None):
    def readArray(f):
        return [float(x) for x in f.readline().split(' ')]

    outputLines = []
    with open(fileName, 'r') as fi:
        runs = int(fi.readline())
        for i in range(1, runs + 1):
            farmCost, farmBenefit, winReq = readArray(fi)
            if not runOnly or i in runOnly:
                seconds = solveB(farmCost, farmBenefit, winReq).compute()
                #print seconds
                outputLines.append("Case #%i: %.8f\n" % (i, seconds))

    with open("output.txt", 'w') as fo:
        fo.writelines(outputLines)

Run("input.txt")