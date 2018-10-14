import math
import sys

def main(inputFilePath):
  cases = []
  try:
    inFile = open(inputFilePath, "r")

    try:
      caseCount = int(inFile.readline())
      for i in xrange(0,caseCount):
        cases.append(inFile.readline().split())

      inFile.close()

    finally:
      inFile.close()

  except IOError:
    print "Error reading from file!"

  for i in xrange(0, len(cases)):
    print "Case #%d: %d" % (i+1, caseResult(cases[i]))

def caseResult(case):
  L = float(case[0])
  P = float(case[1])
  C = int(case[2])


  if(L*C >= P): return 0

  return math.ceil(math.log(math.log(P/L, C),2))


if __name__ == "__main__":
  if(len(sys.argv) > 1):
    main(sys.argv[1])
  else:
    print "Supply input file"


