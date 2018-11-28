from decimal import *

results = []
for t in xrange(input()):
  costPerFarm, clicksPerFarm, goalCookies = [Decimal(x) for x in raw_input().split()]
  clicksPerSec = Decimal(2)
  currCookies = Decimal(0)
  elapsedTime = Decimal(0)
  while True:
    numToClick = (goalCookies / clicksPerSec)
    numToFarm = (costPerFarm / clicksPerSec) 
    numToBuy = numToFarm + (goalCookies / (clicksPerSec + clicksPerFarm))
    if numToClick < numToBuy:
      elapsedTime += numToClick
      break
    else:
      elapsedTime += numToFarm
      clicksPerSec += clicksPerFarm
  results.append("Case #%d: %.7f" % (t + 1, elapsedTime))
print "\n".join(results)

