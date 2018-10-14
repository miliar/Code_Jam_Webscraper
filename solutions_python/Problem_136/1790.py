#!/usr/bin/python
import sys

from random import randint,randrange
import random
import sys, getopt
import argparse
import numpy as np

f= open("2.txt", "r")

numCases=int(f.readline().rstrip('\n'))
case=0

while True:

    case +=1
    if case > numCases:
       break
    
    values = f.readline().rstrip('\n')
    values = values.split(' ')

    C = float(values[0])
    F = float(values[1])
    X = float(values[2])
    rate=2.0
    secs=0.0
    total=0.0
    if not X: break 

    while (total < X):
      if (X-total)/rate < (X-total+C)/(rate+F):
        secs += (X-total)/rate
        total += X -total
      elif total < C:
        secs += (C-total)/rate
        total += C -total

      else:
        total -= C
        rate += F


    print "Case #" + str(case) + ": " + str(secs)
