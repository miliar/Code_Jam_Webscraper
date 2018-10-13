f = open('A-small-practice.in', 'r')
g = open('output.txt', 'w')

"""
def timeCalculator(C, F, X, time, currRate, prevTime):
   #find time to reach X if no Cookie Farm is bought
   timeWithoutCF = time

   #find time to reach X if a Cookie Farm is bought
   nextRate = currRate + F               #increased rate for when a farm is bought     
   buyFarmTime = prevTime + C/currRate   #time taken to buy a farm
   timeAfterBoughtFarm = X/nextRate      #time taken to reach cookie goal after farm is bought
   timeWithCF = buyFarmTime + timeAfterBoughtFarm   #total time taken to reach goal

   #if total time without a new CF is shorter than buying CF, return timeWithoutCF
   if (round(timeWithoutCF, 7) < round(timeWithCF, 7)):
      return round(timeWithoutCF, 7)
   else:
      return timeCalculator(C, F, X, timeWithCF, nextRate, buyFarmTime)
"""

numTestCases = int(f.readline())

#initialCookies = 0, initialRate = 2cookies/s
#C = price of cookie farm
#F = increase rate of cookies
#X = final number of cookies
i = 0
while (i < numTestCases):
   CFX = map(float, (f.readline()).split())
   print CFX
   C = CFX[0]
   F = CFX[1]
   X = CFX[2]

   #find time to reach X if no Cookie Farm is bought
   currRate = 2
   timeWithoutCF = X/currRate
   timeWithCF = 0
   prevTime = 0
   totalTime = 0
   nextRate = currRate + F
   
   while (timeWithoutCF > timeWithCF):
      if (timeWithCF != 0):
         timeWithoutCF = timeWithCF
         currRate = nextRate
         prevTime = totalTimeTakenToBuyFarms

      nextRate = currRate + F
      totalTimeTakenToBuyFarms = prevTime + C/currRate
      timeToReachGoal = X/nextRate

      timeWithCF = totalTimeTakenToBuyFarms + timeToReachGoal
      

      if (timeWithoutCF <= timeWithCF):
         totalTime = round(timeWithoutCF, 7)
         break

   #totalTime = timeCalculator(CFX[0], CFX[1], CFX[2], timeWithoutCF, INITIAL_RATE, 0)
   print("Case #" + str(i+1) + ": " + str(totalTime) + "\n")
   i = i + 1

f.close()
g.close()
   





