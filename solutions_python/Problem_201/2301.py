import math
  
def solve(N, K):
  # Solution here
  setID = int(math.floor(math.log(K, 2)))
  setSize = 2**setID
  targetSum = N - setSize + 1
  
  baseVal = targetSum // setSize
  rem = targetSum % setSize
  
  posInSet = K - setSize + 1
  if posInSet <= rem:
    baseVal += 1
  
  maxVal = baseVal//2
  minVal = ((baseVal-1)//2 if (baseVal-1)//2 >= 0 else 0)
  return [maxVal, minVal]
    
  
##############################################################################

filename = "C-small-2-attempt0.in"
outFile = "solution_stall.txt"
inputFile = open(filename, 'r')
numCases = int(inputFile.readline())
outputFile = open(outFile, 'w')

for case in range(0, numCases):
  N, K = map(int, inputFile.readline().split(" "))
  maxVal, minVal = solve(N, K)
  outputFile.write("Case #{}: {} {}\n".format(case+1, maxVal, minVal))
  
outputFile.close()

# Show result
print(open(outFile,'r').read())
  