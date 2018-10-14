import sys
from itertools import product
    
iFile = open(sys.argv[1],"r")

T = int(iFile.readline().strip())

for i in range(T):

  line = iFile.readline().strip().split()
  
  M = int(line[0])
  N = int(line[1])
  
  S = []
  
  for m in range(M):
    S.append(iFile.readline().strip())
  
  maxNodes = 0
  numWays = 0
  
  for schedule in product(range(N),repeat=M):
    
    Ti = []
    Ti2 = []
    for n in range(N):
      Ti.append(set())
    
    for m in range(M):
      Ti[schedule[m]].add(S[m])
    
    for ti in Ti:
      if ti:
        ti2 = set()
        for x in ti:
          for l in range(len(x)+1):
            ti2.add(x[0:l])
        Ti2.append(ti2)
      else:
        break
    else:
      fullLen = 0
      for ti in Ti2:
        fullLen += len(ti)
      if fullLen > maxNodes:
        maxNodes = fullLen
        numWays = 1
      elif fullLen == maxNodes:
        numWays += 1
        
    
  
  output = str(maxNodes)+" "+str(numWays)
  
  print("Case #"+str(i+1)+": "+output)
