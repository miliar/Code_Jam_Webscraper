#!/usr/bin/python2

import operator
import math

inFile = open ("C-small-attempt0.in", "r")
outFile = open ("outputs.out", "w")
empty_flag = False

def main ():
  
  global empty_flag
  global inFile
  global outFile
  
  numOfCases = int (inFile.readline())
  for i in range (0, numOfCases):
    line = inFile.readline ()
    lst = [int (n) for n in line.split ()]
    count = 0
    # Read single test case
    for x in range (lst[0], lst[1] + 1):
      if compute_pal (x) == True:
        tmp = math.sqrt (x)
        if tmp / int (tmp) != 1:
          continue
        else:
          if compute_pal (int (tmp)) == True:
            count += 1
    outFile.write ("Case #" + str (i + 1) + ": " + str (count) + "\n")
         
  outFile.close ()
  inFile.close ()

def compute_pal (n):
  num = n
  rev = 0
  while num >= 10:
    digit = num % 10
    rev = rev * 10 + digit
    num = num / 10
  else:
    rev = rev * 10 + num;
    
  return rev == n

main ()
