#!/usr/bin/env python
import sys
from decimal import *

def solve():
  rate = Decimal(2.0)
  time = Decimal(0.0)
  currTime, prevTime = None, None
  cookies = Decimal(0.0)
  (c, f, x) = map(Decimal, sys.stdin.readline().split())

  def timeWithoutBuying():
    return time + ((x - cookies) / rate)

  while True:
    currTime = timeWithoutBuying()

    if prevTime != None and currTime > prevTime:
      return str(prevTime.quantize(Decimal('0.000000001')))

    secToFarm = c / rate
    time += secToFarm
    rate += f
    prevTime = currTime

tests = int(sys.stdin.readline())
for case in xrange(1, tests + 1):
  result = solve()
  print "Case #%d: %s" % (case, result)
