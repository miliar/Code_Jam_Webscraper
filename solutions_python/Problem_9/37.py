def parseInput(fileName): # Parses the input
  h = open(fileName)
  n = int(h.readline())
  res = [] # Array of parsed input
  for i in range(0, n):
    K = int(h.readline())
    line = h.readline()
    line = line[0:len(line)-1]
    res.append([K, line.split(" ")])
  # Close file and return result
  h.close()
  return res
        
def newBuildPerfect(K):
  res = [0]*K
  emp = []
  for i in range(0, K):
    emp.append(i)
  p = 0
  for i in range(1, K+1):
    p += i - 1
    p %= len(emp)
    res[emp[p]] = i
    emp.pop(p)
  # Return the result
  return res

def buildPerfect(K):
  res = [0]*K
  u = 0
  p = 0
  i = 1
  while i <= K:
    if not(res[p]):
      u += 1
    if u == i:
      res[p] = i
      u = 0
      i += 1
    p += 1
    if (p == K):
      p = 0
  # Return the perfect deck
  return res

def solve(params):
  K = params[0]
  n = int(params[1][0])
  ds = params[1]
  pd = newBuildPerfect(K)
  res = ""
  for i in range(1, n+1):
    res += str(pd[int(ds[i])-1]) + " "
  res = res[0:len(res)-1]
  return res

inputs = parseInput("C-small-attempt1.in") # Parse the input
outputs = ""
for i in range(0, len(inputs)): # Loop over all cases
  print i
  outputs += "Case #" + str(i+1) + ": " + str(solve(inputs[i])) + "\n"
# Write output to file
h = open("prob-C.out", "w")
h.write(outputs)
h.close()
