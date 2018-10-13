#!/usr/bin/python
import sys

from random import randint,randrange
import random
import sys, getopt
import argparse
import numpy as np

f= open("1.txt", "r")
line=0
numCases=f.readline().rstrip('\n')
found=[]
found2=[]
case=0
while True:

    case +=1
    if case > numCases:
       break
    
    firstGuess = f.readline().rstrip('\n')
    firstSet1 = f.readline().rstrip('\n')
    firstSet2 = f.readline().rstrip('\n')
    firstSet3 = f.readline().rstrip('\n')
    firstSet4 = f.readline().rstrip('\n')
    secGuess = f.readline().rstrip('\n')
    secSet1 = f.readline().rstrip('\n')
    secSet2 = f.readline().rstrip('\n')
    secSet3 = f.readline().rstrip('\n')
    secSet4 = f.readline().rstrip('\n')

    if not secSet4: break 

    if firstGuess == "1":
        found=firstSet1
    if firstGuess == "2":
        found=firstSet2
    if firstGuess == "3":
        found=firstSet3
    if firstGuess == "4":
        found=firstSet4

    if secGuess == "1":
        found2=secSet1
    if secGuess == "2":
        found2=secSet2
    if secGuess == "3":
        found2=secSet3
    if secGuess == "4":
        found2=secSet4
    
    found = set(found.split(' '))
 
    found2 = set(found2.split(' '))

    u = set.intersection(found, found2)

    if len(u) == 0:
      print "Case #" + str(case) + ": " + str("Volunteer cheated!")
      continue

    if len(u) == 1:
      print "Case #" + str(case) + ": " + str(u.pop())
      continue
    if len(u) > 1:
      print "Case #" + str(case) + ": " + str("Bad magician!")
      continue


sys.exit(0)
for i in file.readlines():
  if i == 0:
    numCases=line
    continue
  print line
