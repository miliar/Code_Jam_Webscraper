def read(fileName):
  f = open(fileName, 'r')
  caseNo = int(f.readline())
  P = []
  for i in xrange(caseNo):
    line = f.readline().split()
    X = int(line[0])
    R = int(line[1])
    C = int(line[2])
    P.append([X, R, C])
  return P


def solve(problem):
  X = problem[0]
  R = problem[1]
  C = problem[2]
  if (R > C):
    R, C = C, R

  if ((R * C) % X != 0):
    return 'RICHARD'
  elif (X >= 7):
    return 'RICHARD'
  elif (X <= R):
    return 'GABRIEL'
  elif (X >= C + 1):
    return 'RICHARD'
  elif (X >= 2 * R + 1):
    return 'RICHARD'
  elif (R == 2 and X >= 4):
    return 'RICHARD'
  else:
    return 'GABRIEL'


def write(A):
  f = open("D.out", 'w')
  for i in xrange(len(A)):
    f.write("Case #%s: %s\n" % (i + 1, A[i]))


if __name__=="__main__":
  P = read("D.in")
  A = []
  for problem in P:
    A.append(solve(problem))
  write(A)
