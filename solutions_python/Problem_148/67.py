import sys

iFile = open(sys.argv[1],"r")

T = int(iFile.readline().strip())

for i in range(T):

  line = iFile.readline().strip().split()
  
  N = int(line[0])
  X = int(line[1])
    
  line = iFile.readline().strip().split()
  
  items = [int(a) for a in line]
  
  items.sort(reverse=True)
  
  discs = []
  
  numDiscs = 0
  
  for item in items:
      for disc in discs:
        if disc >= item:
          discs.remove(disc)
          break
      else:
        numDiscs += 1
        discs.append(X - item)
        
  
  output = str(numDiscs)
  
  print("Case #"+str(i+1)+": "+output)
