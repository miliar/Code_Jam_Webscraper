import sys
import math

path = "/Users/yongc0916/Downloads/"
testFile = open(path + "prob2.in", 'r')
fil = open(path+"prob2out.txt", 'w+')
rlist = testFile.readlines()
rlist = rlist[1:]
num = 1

def cookieTime(C, F, X, curr_F, totalTime):
   global num
   if (((X - C) / curr_F) > (X/(curr_F + F))):
      cookieTime(C, F, X, curr_F + F, totalTime + C/curr_F)
   else:
      ans = str.format("{0:.7f}", (totalTime + X/curr_F))
      print ans
      fil.write("Case #" + str(num) + ": " + ans + "\n")
      num += 1

for line in rlist:
   [C,F,X] = line.split()
   C = float(C)
   F = float(F)
   X = float(X)
   ans = cookieTime(C, F, X, 2, 0.0)

fil.close()