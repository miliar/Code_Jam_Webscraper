import os
import re
from sys import *

infile = open(argv[1],"r")
outfile = open(argv[1] + "out","w")
line = infile.readline()
L = int(line.split()[0])
nWords = int(line.split()[1])
nCases = int(line.split()[2])
words = []

for i in range(0,nWords):
  words+=[infile.readline()]
##print (len(words))

for i in range(0, nCases):
  counter = 0;
  case=infile.readline()
  for w in words:
  #  print ("Pattern:" + case.replace('(','[').replace(')',']'))
  #  print ("word" + w)
    pattern = re.compile(case.replace('(','[').replace(')',']'))
    if not (pattern.match(w) is None):
      counter+=1
  outfile.write("Case #" +str(i+1) +": " + str(counter) + '\n')
outfile.close()