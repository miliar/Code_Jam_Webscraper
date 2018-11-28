# -*- coding: utf-8 -*-

import sys


gDbgLvl = 0
maxLvl = 0
     
def main():   
  
  T = int(sys.stdin.readline())
      
  
  logMsg("T = " + str(T))
  
  for t in range(1, T+1):
      
      line = (sys.stdin.readline())
    
      testCase = line.split();  
      farmCost = float(testCase[0])
      farmRate = float(testCase[1])
      goal = float(testCase[2])    
      
      answer = solve2(farmCost, farmRate, goal, 0, 2)
          
      print("Case #" + str(t) + ": " + str(answer))
  
  logMsg("maxLvl " + str(maxLvl), 1)

def solve2(farmCost, farmRate, goal, elapsed, cookiesPerSecond):
    done = 0
    level = 0
    elapsed = 0
    global maxLvl

    logMsg("Elapsed " + str(elapsed))
    logMsg("FarmRate " + str(farmRate))
    logMsg("Goal " + str(goal))

 
    while (done == 0):
        timeToWin = goal / cookiesPerSecond
        timeToBuyFarm = farmCost / cookiesPerSecond
        totalTimeToWin = elapsed + timeToWin
        if (level == 0):
            best = totalTimeToWin
        if (totalTimeToWin < best):
            best = totalTimeToWin
        if (best < elapsed + timeToBuyFarm):
            done = 1;
        elapsed = elapsed + timeToBuyFarm
        cookiesPerSecond = cookiesPerSecond + farmRate
        level = level + 1

    logMsg( "level " + str(level), 3)

    if (level > maxLvl):
        maxLvl = level
        
    return best

def logMsg(str, lvl = 1):
    if (gDbgLvl >= lvl):
      print(str);


main()