import math

def solve(L, P, C):
  # Data conversion.
  L = float(L)
  P = float(P)
  C = int(C)

  # [L, P) takes only K queries if:
  # P = L * C ^ (2 ^ K)
  K = math.log(math.log(P / L, C), 2)

  if K < 0:
    K = 0
  else:
    K = int(math.ceil(K))
  if K == 0:
    if L * C < P:
      print 'Wrong for %s %s %s' % (L, P, C)
  return K

def main():
  FILENAME = 'load'
  f = open('%s.in' % FILENAME, 'r')
  g = open('%s.out' % FILENAME, 'w')

  T = int(f.readline().strip())

  for i in xrange(1, T+1):
    # Read testcase.
    L, P, C = f.readline().strip().split()

    # Solve testcase.
    result = solve(L, P, C)

    # Print testcase.
    g.write('Case #%s: %s\n' % (i, result))
    # print 'Case #%s: %s' % (i, result)

  f.close()
  g.close()

if __name__ == '__main__':
  main()
  print 'Done.'
