table = [[0, 0, 0, 0, 0],
         [0, 1, 2, 3, 4],
         [0, 2,-1, 4,-3],
         [0, 3,-4,-1, 2],
         [0, 4, 3,-2,-1]]


def read(fileName):
  f = open(fileName, 'r')
  caseNo = int(f.readline())
  P = []
  for i in xrange(caseNo):
    line = f.readline().split()
    L = int(line[0])
    X = int(line[1])
    S = []
    for c in f.readline():
      if (c == 'i'):
        S.append(2)
      elif (c == 'j'):
        S.append(3)
      elif (c == 'k'):
        S.append(4)
    P.append([L, X, S])
  return P


def multiply(a, b):
  ret = table[abs(a)][abs(b)]
  if (a * b < 0):
    ret = -1 * ret
  return ret


def PI(S):
  ret = S[0]
  for i in xrange(1, len(S)):
    ret = multiply(ret, S[i])
  return ret


def power(a, x):
  ret = a
  for i in xrange(x - 1):
    ret = multiply(ret, a)
  return ret


def findI(S, X):
  ret = S[0]
  index = 0
  for i in xrange(1, len(S)):
    if (ret == 2):
      return index
    else:
      ret = multiply(ret, S[i])
      index += 1
  for j in xrange(1, X):
    for i in xrange(0, len(S)):
      if (ret == 2):
        return index
      else:
        ret = multiply(ret, S[i])
        index += 1

  return index


def findK(S, X):
  ret = S[-1]
  index = len(S) * X - 1
  for i in xrange(len(S) - 2, -1, -1):
    if (ret == 4):
      return index
    else:
      ret = multiply(S[i], ret)
      index -= 1
  for x in xrange(1, X):
    for i in xrange(len(S) - 1, -1, -1):
      if (ret == 4):
        return index
      else:
        ret = multiply(S[i], ret)
        index -= 1

  return index


def solve(problem):
  L = problem[0]
  X = problem[1]
  S = problem[2]
  ret = 'NO'
  if (power(PI(S), X) == -1 and (findI(S, X) < findK(S, X))):
    ret = 'YES'
  return ret


def write(A):
  f = open("C.out", 'w')
  for i in xrange(len(A)):
    f.write("Case #%s: %s\n" % (i + 1, A[i]))


if __name__=="__main__":
  P = read("C.in")
  A = []
  for problem in P:
    A.append(solve(problem))
  write(A)
