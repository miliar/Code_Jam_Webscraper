import itertools
import math

def readfile(filename):
  """
    Read yon file.

    T
    blah
    blah
    blah
    ...
  """

  retval = []

  with open(filename, "rt") as file:
    T = int(file.readline().strip())

    for i in range(T):
      retval.append(file.readline().strip())

  return retval

def digitsInBase(b):
  return set([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38][:b])

def valueInBase(digits, b):
  val = 0

  while len(digits) > 0:
    val = val + digits[0]
    digits = digits[1:]

    if len(digits) > 0:
      val = val * b

  return val

def findMinHelper(str, base, digitMap, excluded, found, curVal, curMin):
  if not str:
    return curVal

  c = str[0]

  # Have we already allocated this digit?
  if c in found:
    d = digitMap[c]
    curVal = curVal + d * math.pow(base, len(str) - 1)

#    print "using %d = %d" % (d, curVal)

    if (curMin or curMin == 0) and (curVal > curMin):
      return curMin
    else:
      return findMinHelper(str[1:], base, digitMap, excluded, found, curVal, curMin)

  # Check possibilities
  for d in digitsInBase(base):
    if d in excluded:
      continue

    if (len(found) == 0) and (d == 0):
      # 0 can't be first
      continue

    min = curVal + d * math.pow(base, len(str) - 1)

    if (curMin or curMin == 0) and (min > curMin):
      return curMin

    digitMap[c] = d

    min = findMinHelper(str[1:], base, digitMap, excluded | set([d]), found | set(c), min, curMin)

    del digitMap[c]

    if min:
      if (curMin and min < curMin) or (not curMin and curMin != 0):
        curMin = min

  return curMin

def findMin(str):
  uniqueLetters = len(set(str))
  minBase = len(set(str))

  b = minBase
  min = None

  for b in range(minBase, 37):
    m = findMinHelper(str, b, {}, set(), set(), 0, min)

#    print "S: %s in base %d returned %s" % (str, b, m)

    if (min and m < min) or (not min and min != 0):
      min = m

  return min

def process(data):
  i = 1
  for str in data:
    min = findMin(str)

    if min:
      print "Case #%d: %d" % (i, min)
    else:
      print "Case #%d: None" % (i, )
    i = i + 1

#process(readfile("A-sample.in"))
process(readfile("A-small-attempt0.in"))

#print valueInBase([1,1,0,0,1,0,0,1], 2)
#print valueInBase([1,2,3], 10)
#print valueInBase([1,13], 16)
#print digitsInBase(10)
#print digitsInBase(16)
