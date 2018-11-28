import sys
import numpy

iFile = open(sys.argv[1],"r")

T = int(iFile.readline().strip())

for i in range(T):

  N = int(iFile.readline().strip())

  line = iFile.readline().strip().split()
  
  sequence = [int(a) for a in line]
  
  swaps = 0
  
  while len(sequence) > 2:
    
    minPos = numpy.argmin(sequence)
    
    swaps += min(minPos,len(sequence)-1-minPos)
    
    sequence.pop(minPos)
  
  output = str(swaps)
  
  print("Case #"+str(i+1)+": "+output)
