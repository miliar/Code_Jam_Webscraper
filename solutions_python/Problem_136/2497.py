#!/usr/bin/python
import sys

class CookieStrategy:
    
    def __init__(self, C, F, X):
        self.C = C
        self.F = F
        self.X = X
        self.R = 2.0
        self.timeXFarms = {}
        self.optimalTime = 0

    # Time to buy N farms
    def timePurchaseNumberFarms(self, N):
        if (N == 0): return 0
        if (N in self.timeXFarms): return self.timeXFarms[N]
        self.timeXFarms[N] = self.timePurchaseNumberFarms(N-1) + self.C/((N-1)*self.F+self.R)
        return self.timeXFarms[N]

    # Time to reach cookie goal given buying N farms
    def timeCookieGoal(self, N):
        return self.timePurchaseNumberFarms(N) + self.X/(N*self.F+self.R)

    # Optimal time to win Cookies
    def getOptimalTime(self):
        if (self.optimalTime > 0): return self.optimalTime

        # Initialize variables
        x = 0
        prevTime = float("inf")
        time = float("inf")

        # Loop until time for N farms > time for N-1 farms
        while True:
            time = self.timeCookieGoal(x)
            if (time > prevTime):
                optimalTime = prevTime
                return optimalTime
            x = x+1
            prevTime = time
    
if __name__ == "__main__":
   f = open(sys.argv[1], 'r')
   numCases = int(f.readline())
   for x in xrange(numCases):
       inputParams = f.readline().split()
       C = float(inputParams.pop(0))
       F = float(inputParams.pop(0))
       X = float(inputParams.pop(0))
       cookieStrategy = CookieStrategy(C, F, X)
       print "Case #" + str(x+1) + ": " + "%.7f" % cookieStrategy.getOptimalTime()
