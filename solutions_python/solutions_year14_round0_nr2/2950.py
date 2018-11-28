import sys


def calculateTime(farmCost, cpsIncrementer, cookieGoal,):
    totalTime = 0.0
    cookiesPerSec = 2.0

    while(True):
        if (cookieGoal / cookiesPerSec) < ((farmCost/cookiesPerSec) + (cookieGoal / (cookiesPerSec + cpsIncrementer))):
            return totalTime + (cookieGoal/cookiesPerSec)
        else:
            totalTime += farmCost / cookiesPerSec
            cookiesPerSec += cpsIncrementer     
    

#Opening File
try:
    inputFile = open(sys.argv[1], 'r')
except Exception:
    sys.exit("Could not open file, program terminating")


totalCases = inputFile.readline()


for case in range(1, int(totalCases) + 1):
   farmCost, cpsIncrementer, cookieGoal = inputFile.readline().split() 
   totalTime = calculateTime(float(farmCost), float(cpsIncrementer), float(cookieGoal))
   print('Case #' + str(case) + ': ' + "%.7f" % totalTime)
