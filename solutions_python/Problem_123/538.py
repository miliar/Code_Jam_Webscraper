import sys
from math import *

# Functions
def MakeSolvable(currentSize, motes):
  while len(motes) > 0:
    m = motes[0]
    del motes[0]
    if currentSize > m:
      currentSize += m
      continue
    elif currentSize <= 1:
      return len(motes) + 1
    else:
      deletionOps = len(motes) + 1      # Add one because we also delete the current mote
      addOps = 0
      while currentSize <= m:
        currentSize += currentSize - 1
        addOps += 1
      addOps += MakeSolvable(currentSize + m, motes)    # Solve the rest of the list as well
      if deletionOps <= addOps:
        return deletionOps
      else:
        return addOps
  return 0

# Script
fptr = open(sys.argv[1], "r")
content = fptr.readlines()
numCases = int(content[0])
del content[0]
i=1

while len(content) > 0:
  x = content[0].split()
  del content[0]
  mySize = int(x[0])
  numMotes = int(x[1])
  motes = content[0].split()
  del content[0]
  motes = [int(m) for m in motes]
  motes.sort()
  operations = MakeSolvable(mySize, motes)
  print "Case #%d: %d" % (i, operations)
  i+=1
