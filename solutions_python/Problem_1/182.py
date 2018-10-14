import sys

sys.setrecursionlimit(10000)

def minSwitches(engines, queries):
   maxFarIn = 0
   for e in engines:
      farIn = 0
      for q in queries:
         if q == e:
            break;
         farIn += 1
      if farIn > maxFarIn:
         maxFarIn = farIn
   if maxFarIn == len(queries):
      return 0
   else:
      return minSwitches(engines,queries[maxFarIn:]) + 1

N = int(sys.stdin.readline())

for i in range(1, N + 1):
   S = int(sys.stdin.readline())
   engines = []
   for j in range(S):
      engines.append(sys.stdin.readline().strip())
      
   Q = int(sys.stdin.readline())
   queries = []
   for j in range(Q):
      queries.append(sys.stdin.readline().strip())

   print "Case #%d: %d" %(i, minSwitches(engines, queries))


