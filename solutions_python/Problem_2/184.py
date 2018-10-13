import sys

class time(object):
   def __init__(self, timestr):
      h, m = timestr.split(":")
      self.h = int(h)
      self.m = int(m)

   def __cmp__(self, other):
      if self.h < other.h:
         return -1
      if self.h > other.h:
         return 1
      if self.h == other.h:
         if self.m < other.m:
            return - 1
         if self.m > other.m:
            return 1
      return 0

   def addMins(self, mins):
      self.m += mins
      if self.m >= 60:
         self.m -= 60
         self.h += 1

   def __str__(self):
      return "%2d:%2d" %(self.h, self.m)

   def __repr__(self):
      return self.__str__()


N = int(sys.stdin.readline())

for i in range(1, N + 1):
   T = int(sys.stdin.readline())
   NA, NB = sys.stdin.readline().strip().split()
   NA = int(NA)
   NB = int(NB)

   ADepart = []
   BArrival = []
   for j in range(NA):
      adep, barr = sys.stdin.readline().strip().split()
      ADepart.append(time(adep))
      t = time(barr)
      t.addMins(T)
      BArrival.append(t)

   BDepart = []
   AArrival = []
   for j in range(NB):
      bdep, aarr = sys.stdin.readline().strip().split()
      BDepart.append(time(bdep))
      t = time(aarr)
      t.addMins(T)
      AArrival.append(t)

   ADepart.sort()
   BDepart.sort()
   AArrival.sort()
   BArrival.sort()

   numA = 0
   numB = 0

   for j in ADepart:
      if len(AArrival) > 0:
         if AArrival[0] <= j:
            AArrival.pop(0)
            continue
      numA += 1

   for j in BDepart:
      if len(BArrival) > 0:
         if BArrival[0] <= j:
            BArrival.pop(0)
            continue
      numB += 1

   print "Case #%d: %d %d" %(i, numA, numB)
      

