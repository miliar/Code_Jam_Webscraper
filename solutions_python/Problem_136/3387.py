import sys,os
from sys import stdin
sys.setrecursionlimit(10000)

testCase = int(stdin.readline())


#1st if normal rate < time needed to buy farm
def compareWithNormalRate(secAfterBuyFarm,currentRate,targetCookies,secondNeeded):
    autoGenerate = targetCookies/currentRate + secondNeeded
    #print "auto" + str(autoGenerate)
    if secAfterBuyFarm > autoGenerate:
        return True
    else:
        return False

def secondToBuyFarm(farmCost, currentRate, targetCookies,extraCookies, case,secondNeeded = 0.0):
    compare = False
    #new rate after buy farm
    newRate = currentRate + extraCookies
    #total time needed after buying farm
    secAfterBuyFarm = farmCost/currentRate + targetCookies/newRate + secondNeeded
    totalTimeNeeded = secondNeeded + targetCookies/currentRate
    
    #first case: if total time after buying farm > auto generate is true
    #dont need to buy farm, just auto generate + previuous time need to buy farm
    if totalTimeNeeded < secAfterBuyFarm:
        result = secondNeeded + targetCookies/currentRate
        print "Case #%d: %f"% (case, result)
        #yield result 
        
        #print "Case #%d: %f"% (case, result)
        return 
    #case 2: if normal rate take > time take enough to buy farm
    #check if the buy another farm generate faster current one
    elif compare == False:
        secondNeeded = secondNeeded + farmCost/currentRate
        #compare new rate, if current generate faster then then new rate
        nextRate = newRate + extraCookies
        nextFarm = farmCost/(newRate) + secondNeeded
        totalTimeForNextFarm = nextFarm + targetCookies/nextRate
        if secAfterBuyFarm < totalTimeForNextFarm:
            #print "Case #%d: %f"% (case, secAfterBuyFarm)
            #yield secAfterBuyFarm
            print "Case #%d: %f"% (case, secAfterBuyFarm)
            return 
        else:
            secondToBuyFarm(farmCost, currentRate+extraCookies, targetCookies, extraCookies, case,secondNeeded )

for i in range(0, testCase):
    #read input
    readInput = stdin.readline()
    inputNo = [float(x) for x in readInput.split()]
    secondToBuyFarm(inputNo[0], 2.0,  inputNo[2],inputNo[1], i+1,secondNeeded=0.0)
    #for each in (secondToBuyFarm(inputNo[0], 2.0,  inputNo[2],inputNo[1], i+1,secondNeeded=0.0)):
    #s    print each,
  
  
  
  