#!/usr/local/bin/python2.7
from __future__ import print_function
minRate = 2.0

def calcTime(numTerms, c, f, x) :
  tim = 0
  r = minRate
  for i in range(0, (numTerms-1)) :
    r = minRate + (i*f)
    tim = tim + (c/r)
  r = minRate + ((numTerms-1)*f)
  tim = tim + (x/r)
  return tim
  
file = open("input.txt", 'r')
fileContents = []
for line in file : 
  fileContents.append(line)
numTests = int(fileContents[0])+1
for tC in range(1, numTests) :
  
  nums = [float(n) for n in fileContents[tC].split()]
  c = nums[0]
  f = nums[1]
  x = nums[2]
  cnt = 2
  pTime = calcTime(1, c, f, x)
  currTime= calcTime(2, c, f, x)
  while(currTime < pTime) :
    cnt = cnt +  1
    resTime = calcTime(cnt, c, f, x)
    pTime = currTime
    currTime = resTime
  
  print("Case #",tC,": ",pTime,sep='')
