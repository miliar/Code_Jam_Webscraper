#!/usr/bin/env python
import sys

def is_legal(lawn, lengths, n, m):
   # find the smallest 
   lengths.sort()
   for l in lengths:
      for i in range(0, n):
         for j in range(0, m):
            if (lawn[i][j] == l) and (not check_lines(lawn, i, j, n, m, l)):
               return False
            
   return True
   
def check_lines(lawn, i, j, n, m, length):
   okayX = True
   okayY = True
   for x in range(0, n):
      okayX = okayX and (lawn[x][j] <= length)
   for y in range(0, m):
      okayY = okayY and (lawn[i][y] <= length)
   
   return okayX or okayY
      

# let's do it!

ncases = int(sys.stdin.readline().strip())

for i in range(1, ncases+1):
   (n, m) = [int(x) for x in sys.stdin.readline().strip().split()]
   
   lawn = []
   lengths = []
   # read the lawn
   for _ in range(0, n):
      x = [int(a) for a in sys.stdin.readline().strip().split()]
      lengths.extend([a for a in x if not a in lengths])
      lawn.append(x)
      
   sys.stdout.write("Case #%d: " % i)
   if (is_legal(lawn, lengths, n, m)):
      print("YES")
   else:
      print("NO")
      
