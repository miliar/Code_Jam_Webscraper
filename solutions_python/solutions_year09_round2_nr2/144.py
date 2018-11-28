import os
import re
from sys import *

def isDescending(array):
  return array == sorted(array)[::-1]

if len(argv) == 1:
  infilename = "input"
else:
  infilename = argv[1]
infile = open(infilename,"r")
outfile = open(infilename + "out","w")

line = infile.readline()
cases  = int(line)

for case in range(0,cases):
  line = infile.readline()
  number = int(line)
  numbers = [0] + [int(c) for c in str(int(line))]
  nextnumbers = numbers
  for i in range(-1,-len(numbers)-1,-1):
    quit=False
    if not isDescending(numbers[i:]):
      quit= True
      digit = nextnumbers[i]
      m = min([n for n in numbers[i+1:] if n>digit])
      mindex = (numbers[i+1:]).index(m)
      nextnumbers[i]= m
      nextnumbers[i+1+mindex]= digit
      nextnumbers = nextnumbers[:i+1]+sorted(nextnumbers[i+1:])
    if quit: break

  next = 0
  for digit in nextnumbers:
    next = 10*next + digit
  print next
  outfile.write("Case #" +str(case+1) +": " + str(int(next)) + '\n')
outfile.close()