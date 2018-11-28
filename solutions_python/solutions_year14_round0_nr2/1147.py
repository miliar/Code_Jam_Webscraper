from math import floor
import sys

def main():
   if len(sys.argv) != 2:
      print("Error")
      return
      
   file = open(sys.argv[1], 'r')
   
   b = 2.0
   case = 0
   for line in file:
      if case == 0:
         case += 1
         continue
      vars = line.split()
      C = float(vars[0])
      F = float(vars[1])
      X = float(vars[2])
   
      n = max(int(floor(X/C - b/F)), 0)
   
      time = 0.0
      for i in range(n):
         time += C/(b+i*F)
      time += X/(b+n*F)
   
      print("Case #" + str(case) +  ": " + str(time))
      case += 1
   
main()
   