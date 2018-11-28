import sys

class bf(object):
   def __init__(self,value=0):
      self._d = value

   def __getitem__(self, index):
      return (self._d >> index) & 1

   def __setitem__(self,index,value):
      value    = (value&1L)<<index
      mask     = (1L)<<index
      self._d  = (self._d & ~mask) | value

   def __getslice__(self, start, end):
      mask = 2L**(end - start) -1
      return (self._d >> start) & mask

   def __setslice__(self, start, end, value):
      mask = 2L**(end - start) -1
      value = (value & mask) << start
      mask = mask << start
      self._d = (self._d & ~mask) | value
      return (self._d >> start) & mask

   def __int__(self):
      return self._d

def calculateLightState(snappers, snaps):
   snappers = int(snappers)
   snaps = int(snaps)
   bitField = bf(snaps)
   if bitField[0:snappers] == (2**snappers-1):
      return "ON"
   else:
      return "OFF"

inputFile = open(sys.argv[1])

numberOfCases = int(inputFile.readline())

for i in range(numberOfCases):
   (numberOfSnappers, numberOfSnaps) = inputFile.readline().split()
   print "Case #" + str(i+1) + ": " + calculateLightState(numberOfSnappers, numberOfSnaps)

