#!/usr/bin/python3

import sys

def computeOptim(cost, farmProd, target):
  (timePrev, timeNow) = (0.0, 0.0)
  (prodPrev, prodNow) = (0.0, 2.0)
  part1 = 0 #Farm Productions

  timeNow = target / prodNow

  while True:
    timePrev = timeNow
    prodPrev = prodNow
    prodNow += farmProd
    part1 += (cost / prodPrev)
    timeNow = part1 + (target / prodNow)
    if timeNow > timePrev:
      break
  return timePrev

def parse(filename):
  f = open(filename)
  numTestCases = int(f.readline())
  numtestmax = numTestCases + 1
  while numTestCases:
    print ("Case #" + str(numtestmax - numTestCases) + ": ", end='')
    values = [float(x) for x in f.readline().strip().split(" ")]
    computed = computeOptim(values[0], values[1], values[2])
    print (computed)
#dec numTestCases
    numTestCases -= 1

def main():
  parse(sys.argv[1])

main()
