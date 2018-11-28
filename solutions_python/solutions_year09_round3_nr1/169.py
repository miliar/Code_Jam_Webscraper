import os
import re
from sys import *
def findmin(values):
  if not 0 in values:
    return 0
  else:
    return max(values)+1

if len(argv) == 1:
  infilename = "input"
else:
  infilename = argv[1]
infile = open(infilename,"r")
outfile = open(infilename + "out","w")

line = infile.readline()
cases  = int(line)

for case in range(1,1+cases):
  line = infile.readline()
  digits = [c for c in line.rstrip()]
  base = max(2,len(set(digits)))
  dic = {}
  translation = 0

  while not (len(dic)==base or (base == 2 and len(set(digits)) == 1 and len(dic)==1)):
    for digit in digits:
      if not dic.has_key(digit):
        if digits[0] == digit:
          dic[digit] = 1
        else:
          dic[digit] = findmin(dic.values())
          break
  for digit in digits:
    translation = base * translation + dic[digit]
  print translation
  outfile.write("Case #" +str(case) +": " + str(int(translation)) + '\n')
outfile.close()