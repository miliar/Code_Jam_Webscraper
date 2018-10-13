import sys

dataSetCount = int(sys.stdin.readline().strip())

#print dataSetCount

def calculateTimeToGoal(currentCookies, cookiesPerSecond, goal):
   cookiesNeeded = goal - currentCookies
   return cookiesNeeded / cookiesPerSecond

for i in range(dataSetCount):
   args = sys.stdin.readline().strip().split()
   farmCost = float(args[0])
   cookiesPerFarm = float(args[1])
   winValue = float(args[2])
   #print '%.7f' % farmCost, '%.7f' % cookiesPerFarm, '%.7f' % winValue

   currentCookies = 0.0;
   currentCookiesPerSecond = 2.0;
   elapsedTime = 0.0;

   finished = False
   while finished == False:
      timeToNextFarm = calculateTimeToGoal(currentCookies, currentCookiesPerSecond, farmCost)
      timeToWin = calculateTimeToGoal(currentCookies, currentCookiesPerSecond, winValue)

      #print 'timeToNextFarm: ' + str(timeToNextFarm)
      #print 'timeToWin: ' + str(timeToWin)

      if timeToNextFarm >= timeToWin:
         finished = True
      else:
         # Figure out it if would be faster to build another farm or to win.
         nextCookiesPerSecond = currentCookiesPerSecond + cookiesPerFarm;
         nextTimeToWin = timeToNextFarm + calculateTimeToGoal(0, nextCookiesPerSecond, winValue)
         #print 'nextTimeToWin: ' + str(nextTimeToWin)
         if timeToWin <= nextTimeToWin:
            finished = True
         else:
            # It will be faster to build another farm.
            elapsedTime = elapsedTime + timeToNextFarm
            currentCookiesPerSecond = currentCookiesPerSecond + cookiesPerFarm

      if finished:
         print 'Case #' + str(i + 1) + ': ' + '%.7f' % (elapsedTime + timeToWin)
      #print finished


