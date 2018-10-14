'''
 Codejam

 Problem 2: Cookie's monster

 @author Aaron Fas <yo@aaron.com.es>
'''

import sys

class CookieMonster:
  def __init__(self, farmCost, farmProduction, targetCookies):
    self.farmCost = farmCost
    self.farmProduction = farmProduction
    self.targetCookies = targetCookies
    self.production = 2.0

  def calculate(self):
    seconds = 0
    gotAllCookies = False
    while not gotAllCookies:
      timeToTarget = self.__timeToTarget()
      timeToFarm = self.__timeToNextFarm()
      timeToTargetAfterFarm = self.__timeToTargetAfterFarm()
      if timeToTargetAfterFarm < timeToTarget:
        # No cookies remaining, we ate them ... yum!
        self.production += self.farmProduction
        seconds += timeToFarm
      else:
        seconds += timeToTarget
        gotAllCookies = True
    return seconds

  def __timeToCookies(self, target, production):
    return target / float(production)

  def __timeToNextFarm(self):
    return self.__timeToCookies(self.farmCost, self.production)

  def __timeToTarget(self):
    return self.__timeToCookies(self.targetCookies, self.production)

  def __timeToTargetAfterFarm(self):
    return self.__timeToNextFarm() + self.__timeToCookies(self.targetCookies, self.production + self.farmProduction)

if __name__ == '__main__':
  cases = int(sys.stdin.readline())
  for case in range(1, cases+1):
    configuration = sys.stdin.readline().strip().split(' ')
    farmCost = float(configuration[0])
    farmProduction = float(configuration[1])
    target = float(configuration[2])
    cookieMonster = CookieMonster(farmCost, farmProduction, target)
    seconds = cookieMonster.calculate()
    print "Case #{}: {:.7f}".format(case, seconds)

