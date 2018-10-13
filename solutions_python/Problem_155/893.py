def read(fileName):
  f = open(fileName, 'r')
  caseNo = int(f.readline())
  P = []
  for i in xrange(caseNo):
    line = f.readline().split()
    maxS = int(line[0])
    shy = []
    for c in line[1]:
      shy.append(int(c))
    P.append([maxS, shy])
  return P


def solve(problem):
  maxS = problem[0]
  shy = problem[1]
  ret = 0
  stand = 0
  for i in xrange(maxS + 1):
    if (shy[i] == 0):
      continue

    if (stand < i):
      ret += i - stand
      stand = i
    stand += shy[i]
  return ret


def write(A):
  f = open("A.out", 'w')
  for i in xrange(len(A)):
    f.write("Case #%s: %s\n" % (i + 1, A[i]))


if __name__=="__main__":
  P = read("A.in")
  A = []
  for problem in P:
    A.append(solve(problem))
  write(A)
