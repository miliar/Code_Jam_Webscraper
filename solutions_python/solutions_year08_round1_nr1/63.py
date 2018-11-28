import sys

def parseInput(fname):
  f = open(fname, 'r')
  text = f.readlines()
  f.close()

  testCases = []
  cases = int(text[0])
  cnt = 1
  for i in range(cases):
    case = []
    numCoords = int(text[cnt])
    cnt += 1
    vec1 = text[cnt].strip().split(" ")
    vec1 = [int(t) for t in vec1]
    cnt += 1
    vec2 = text[cnt].strip().split(" ")
    vec2 = [int(t) for t in vec2]
    cnt += 1
    case = (numCoords, vec1, vec2)

    testCases.append(case)
  return testCases


def runCase(case):
  case[1].sort()
  case[2].sort()
  case[2].reverse()
  together = zip(case[1], case[2])
  return sum(a*b for a,b in together)

def main(inputs=["test"]):
  for inputf in inputs:
    cases = parseInput(inputf+".in")
    res = []
    i = 1
    for case in cases:
      res.append((i,runCase(case)))
      i += 1
      
    output = ["\n".join("Case #%s: %s" % (num, ans) for num,ans in res)]
    outf = open(inputf+".out",'w')
    outf.write("\n".join("Case #%s: %s" % (num, ans) for num,ans in res))
    outf.close()

if __name__=="__main__":
  if sys.argv[1:]:
    main(sys.argv[1:])
  else:
    main()
