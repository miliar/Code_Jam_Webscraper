def list2num(numList):
  return int("".join(map(str, numList)))

def solve(N):
  # Solution here
  digits = [int(x) for x in str(N)]
  res = []
  
  M = len(digits)
  
  for k in range(0, M):
    potentialDigit = digits[k]
    for j in range(k+1, M):
      if digits[j] > potentialDigit:
        break
      elif digits[j] < potentialDigit:
        if potentialDigit > 1:
          res.append(potentialDigit-1)
        for n in range(k+1, M):
          res.append(9)
        return list2num(res)
          
    res.append(potentialDigit)
          
  
  return list2num(res)
  
##############################################################################

filename = "B-large.in"
inputFile = open(filename, 'r')
numCases = int(inputFile.readline())
outputFile = open("solution_tidy.txt", 'w')

for case in range(0, numCases):
  N = int(inputFile.readline())
  outputFile.write("Case #{}: {}\n".format(case+1, solve(N)))
  
outputFile.close()

# Show result
print(open("solution_tidy.txt",'r').read())
  