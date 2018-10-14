# -*- coding: utf-8 -*-

import sys


gDbgLvl = 0


     
def main():
  logMsg("In main", 3)
    
  
  T = int(sys.stdin.readline())
  
  logMsg("T = " + str(T))
  
  for t in range(1, T+1):
      
      ans1 = int(sys.stdin.readline())     
      logMsg("Answer #1 = " + str(ans1));
      
      for row in range(1, 5):
          line = sys.stdin.readline()
          if (row == ans1):
              line1 = line;
    
      ans2 = int(sys.stdin.readline())
      logMsg("Answer #1 = " + str(ans1));

      for row in range(1, 5):
          line = sys.stdin.readline()
          if (row == ans2):
              line2 = line;

      logMsg("line1 = " + line1, 3)
      logMsg("line2 = " + line2, 3)

      list1 = line1.split()
      list2 = line2.split()
      

      logMsg("list1: " + str(list1), 1)
      logMsg("list2: " + str(list2), 1)
      
      intersection = list(set(list1) & set(list2))
      logMsg("Intersection" + str(intersection), 1)
      
      print("Case #" + str(t) + ":"),
      
      if (len(intersection) == 1):
          print (intersection[0])
      elif (len(intersection) == 0):
          print "Volunteer cheated!"
      else:
          print "Bad magician!"
  
  
  logMsg("Exiting main", 3)  
  sys.exit()
  

def logMsg(str, lvl = 1):
    if (gDbgLvl >= lvl):
      print(str);


main()