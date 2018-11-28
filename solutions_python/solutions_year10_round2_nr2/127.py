import math
import sys

def main(inputFilePath):
  cases = []
  try:
    inFile = open(inputFilePath, "r")

    try:
      caseCount = int(inFile.readline())
      for i in xrange(0,caseCount):
        N,K,B,T = inFile.readline().split()
        chicks = []
        X = inFile.readline().split()
        V = inFile.readline().split()
        for j in xrange(0,int(N)):
          chicks.append([int(X[j]), int(V[j])])

        cases.append([int(K),int(B),int(T),chicks])


      inFile.close()

    finally:
      inFile.close()

  except IOError:
    print "Error reading from file!"

  for i in xrange(0, len(cases)):
    print "Case #%d: %s" % (i+1, caseResult(cases[i]))
    
def caseResult(case):
  K = case[0]
  B = case[1]
  T = case[2]
  chicks = case[3]
  swapCount = 0
  A = len(chicks) - 1
  i = len(chicks) - 1
  while i >= 0 and K > 0:
    if finishes(B, T, chicks[i]):
      swapCount += (A - i)
      A -= 1
      K -= 1
      
    i -= 1

  if K > 0:
    return "IMPOSSIBLE"
  else:
    return str(swapCount)

def finishes(B, T, chick):
  fT = float(B - chick[0]) / float(chick[1])
  return  fT <= T


if __name__ == "__main__":
  if(len(sys.argv) > 1):
    main(sys.argv[1])
  else:
    print "Supply input file"


