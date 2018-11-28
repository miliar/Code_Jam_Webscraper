
debugEnabled = False
def isrecyc(n, m):
   n = str(n)
   m = str(m)
   k = len(n)
   if k != len(m):
      return False
   if set(m) != set(n):
      return False

   #debug("N: " + n)
   #debug("M: " + m)
   l = 1
   while l <= len(m):
      nn = n[l:] + n[:l]
      #debug("L " + str(l) + " NN:" + nn)
      #print nn
      if int(nn) == int(m):
         return True
      l = l + 1

   
   return False


def doProblem(i, f):
   debug("doing task " + str(i))

   line = f.readline().strip()
   ints = line.split(" ")
   a = int(ints[0])
   b = int(ints[1])
   count = 0
   aa = a
   while aa < b:
      bb = aa + 1
      while bb <= b:
         if isrecyc(aa, bb):
            count = count + 1
         bb = bb + 1 
      aa = aa + 1
   print("Case #" + str(i+1) + ": " + str(count))

   debug("done task " + str(i))

def debug(m):
   if debugEnabled:
      print(m)

import sys
f = open(sys.argv[1],'r')
T = int(f.readline())

debug(str(T) + " tasks")

i = 0
while i < T:
   doProblem(i, f)
   i = i + 1
