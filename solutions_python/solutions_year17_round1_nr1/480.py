import sys

def solve(N):
  last = 0
  for i, x in enumerate(N):
    if all([c == '?' for c in x]):
      last = min(last, i)
    else:
      j = 0
      while j < len(x):
        c = x[j]
        if c != '?':
          f = j - 1
          while f >= 0 and x[f] == '?':
            x[f] = c
            f -= 1

          b = j + 1
          while b < len(x) and x[b] == '?':
            x[b] = c
            b += 1

          j = b

        else:
          j += 1
      for _ in xrange(last, i + 1):
        print ''.join(x)
      last = i + 1
  i = last - 1
  while last < len(N):
    print ''.join(N[i])
    last += 1

def main(argv):
  f = open(argv[1], 'r')
  c = int(f.readline())
  for i in xrange(c):
    print 'Case #%d:' % (i + 1)
    R, C = f.readline().split(' ')
    A = []
    for _ in xrange(int(R)):
      l = [c for c in f.readline()[:-1]]
      A.append(l)
    solve(A)
  f.close()

if __name__ == '__main__':
  main(sys.argv)
