# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
from math import pi
from decimal import *

getcontext().prec = 32

PI = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078')

t = int(raw_input())  # read a line with a single integer

def top(r, h):
  return Decimal(1) * r * r * PI

def side(r, h):
  return Decimal(2) * r * PI * h

def total(r, h):
  return top(r, h) + side(r, h)

def getUpdatedContribution(pancakes, maxR):
  updatedList = list()
  for pancake in pancakes:
    r, h, c = pancake
    if r <= maxR:
      updatedList.append((r, h, side(r, h)))
    else:
      updatedList.append((r, h, side(r, h) + top(r, h) - top(maxR, h)))
  return sorted(updatedList, key=lambda x: x[2])
  

for i in xrange(1, t + 1):
  n, k = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  availablePancakes = list()
  for j in xrange(1, n + 1):
    r, h = [Decimal(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    availablePancakes.append((r, h, total(r, h)));
  # take pancake with biggest surface
  availablePancakes = sorted(availablePancakes, key=lambda x: x[2])
  maxSurface = availablePancakes.pop()
  selectedPancakes = list()
  selectedPancakes.append(maxSurface)
  totalSurface = maxSurface[2]
  maxR = maxSurface[0]
  # we have one pancake, and need k - 1 more
  for x in xrange(1, k):
    # print "Before: ", maxR, availablePancakes
    availablePancakes = getUpdatedContribution(availablePancakes, maxR)
    # print "After: ", availablePancakes
    nextPancake = availablePancakes.pop()
    selectedPancakes.append(nextPancake)
    totalSurface += nextPancake[2]
    maxR = max(maxR, nextPancake[0])
  selectedPancakes = sorted(selectedPancakes, key=lambda x: x[0])
  r, h, c = selectedPancakes.pop()
  totalSurface = total(r, h)
  for pancake in selectedPancakes:
    r, h, c = pancake
    totalSurface += side(r, h)
  print "Case #{0}: {1:.9f}".format(i, totalSurface)




