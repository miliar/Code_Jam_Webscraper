import sys

iFile = open(sys.argv[1],"r")

size = int(iFile.readline().strip())

for i in range(size):

  line = iFile.readline().strip().split()
  
  C = float(line[0])
  F = float(line[1])
  X = float(line[2])
  
  P = 2.0
  
  totaltime = 0.0
   
  while C/P + X/(P+F) < X/P:
    totaltime += C/P
    P += F
    
  totaltime += X/P
  
  output = str(totaltime)
  
  print("Case #"+str(i+1)+": "+output)
